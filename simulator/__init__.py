from path import path
from pyavrutils.arduino import Arduino
from pysimavr.avr import Avr
from pysimavr.connect import connect_pins_by_rule
from pysimavr.firmware import Firmware
from pysimavr.sgm7 import Sgm7
from pysimavr.vcdfile import VcdFile
from pysimavrgui.examples.sim.avrsimmain import AvrSimMain
from pysimavrgui.sgm7game import Sgm7Game
import time

connections_txt = path(__file__).parent / 'connections.txt'
template_cpp = path(__file__).parent / 'template.cpp'

MCU = 'atmega328'
F_CPU = 16000000

TEMPLATE = open(template_cpp).read()


def run_sim(code, vcdfile='sgm7.vcd', speed=0.001, fps=20, timeout=0.0, visible=1, image_file=''):
    arduino = Arduino(f_cpu=F_CPU)
    arduino.build(sources=code)

    firmware = Firmware(arduino.output)
    firmware.f_cpu = F_CPU
    firmware.mcu = MCU
    avr = Avr(firmware)
    vcd = VcdFile(avr, period=1000, filename=vcdfile) if vcdfile else None

    # ###################################################
    # sgm7
    sgm7 = Sgm7(avr, size=4)

    connect_pins_by_rule(open(connections_txt).read(),
                         dict(
                             avr=avr,
                             sgm7=sgm7,
                         ),
                         vcd=vcd,
                         )

    def segments_func(digit_index):
        return (sgm7.digit_segments(digit_index), sgm7.reset_dirty(digit_index))
    sgm7_game = Sgm7Game(segments_func=segments_func, disp_size=4)

    dev = sgm7_game

    scrshot_by_exit = [(dev, image_file)] if image_file else None
    AvrSimMain(
        avr, dev, vcd, speed=speed, fps=fps, visible=visible, timeout=timeout,
        scrshot_by_exit=scrshot_by_exit).run_game()

    time.sleep(1)


def code2size(code):
    arduino = Arduino(f_cpu=F_CPU)
    arduino.build(sources=code)
    size = arduino.size()
    return size


def democode2size():
    code = TEMPLATE.replace('//snippet', 'disp.DisplayString("1234", 3);')
    return code2size(code)


def emty_template_size():
    code = Arduino().minprog
    return code2size(code)


def code2img(snippet, image_file, timeout=0.2):
    code = TEMPLATE.replace('//snippet', snippet)
    run_sim(code=code,
            timeout=timeout,
            vcdfile=None,
            visible=0,
            image_file=image_file,
            speed=1,
                )
