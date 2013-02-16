from paver.easy import *
import csv
import paver.doctools
import paver.misctasks
sys.path.insert(0, path('.').abspath())

try:
    import simulator 
except ImportError:
    pass

try:
    from paved import *
    from paved.dist import *
    from paved.util import *
    from paved.docs import *
except ImportError:
    pass


code_examples = list(path('SevSeg').walkfiles('*.ino'))
docs = path('docs')

options(
    sphinx=Bunch(
        docroot='docs',
        builddir="_build",
    ),
    pdf=Bunch(
        builddir='_build',
        builder='latex',
    ),
)


@task
@needs(
       'screenshot',
       'libsize',
       'html',
       )
def all():
    pass

@task
@needs('screenshot_snippet', 'screenshot_full')
def screenshot():
    pass


@task
def screenshot_full():
    for x in code_examples:
        image_file = docs / ('generated_%s.png' % x.namebase)
        vcdfile = docs / ('generated_%s.vcd' % x.namebase)
        info('generating %s and %s' % (image_file, vcdfile))

        run_sim(code=open(x).read(),
                timeout=0.2,
                visible=0,
                speed=0.2,
                image_file=image_file,
                vcdfile=vcdfile,
                )


@task
def screenshot_snippet():
    '''generate screenshots from code snippets'''
    d = path(options.sphinx.docroot)
    f = open(d / 'code_examples.csv', 'rb')
    reader = csv.reader(f)

    fx = open(d / 'generated_examples.csv', 'wb')
    writer = csv.writer(fx)
    info('generating ' + fx.name)

    path(d / 'generated_template.cpp').write_text(TEMPLATE)

    for i, (src, comment) in enumerate(reader):
        src = src.replace('{LF}', '\n')

        fcode = d / ('generated_code_%02d.cpp' % i)
        path(fcode).write_text(src)
        info('generating ' + fcode)

        fscreen = d / ('generated_disp_%02d.png' % i)
        code2img(src, fscreen)
        info('generating ' + fscreen)

        writer.writerow([
                        comment,
                        '.. literalinclude:: ' + fcode.name,
                        '.. image:: ' + fscreen.name,
                        ])


@task
def libsize():
    '''calculate lib size'''
    d = path(options.sphinx.docroot)

    fx = open(d / 'generated_code_sizes.csv', 'wb')
    writer = csv.writer(fx)
    info('generating ' + fx.name)

#    path(d / 'generated_template.cpp').write_text(TEMPLATE)
    empty_size = emty_template_size()
    size = democode2size()
    writer.writerow([
                    size.program_bytes - empty_size.program_bytes,
                    size.data_bytes - empty_size.data_bytes,
                    ])


@task
def example():
    'start first example'
    simulator.run_sim(
        code=open(code_examples[0]).read(),
        # timeout=timeout,
        vcdfile=None,
        visible=1,
        # image_file=image_file,
        speed=0.02,
    )


options.paved.clean.patterns += ['*.pickle',
                                 '*.doctree',
                                 'generated_*',  # generated files
                                 ]
