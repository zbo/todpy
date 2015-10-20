__author__ = 'bob.zhu'
import os
import sys
import optparse
import lettuce
import pdb

def main(args=sys.argv[1:]):
    base_path = os.path.join(os.path.dirname(os.curdir), 'features')
    parser = make_parser()

    options, args = parser.parse_args(args)
    if args:
        base_path = os.path.abspath(args[0])

    try:
        options.verbosity = int(options.verbosity)
    except ValueError:
        pass

    tags = None
    if options.tags:
        tags = [tag.strip('@') for tag in options.tags]

    runner = lettuce.Runner(
        base_path=base_path,
        scenarios=options.scenarios,
        verbosity=options.verbosity,
        random=options.random,
        enable_xunit=options.enable_xunit,
        xunit_filename=options.xunit_file,
        enable_subunit=options.enable_subunit,
        subunit_filename=options.subunit_filename,
        failfast=options.failfast,
        auto_pdb=options.auto_pdb,
        tags=tags,
        root_dir=options.root_dir,
    )

    result = runner.run()
    failed = result is None or result.steps != result.steps_passed
    raise SystemExit(int(failed))


def make_parser():
    parser = optparse.OptionParser(
        usage="%prog or type %prog -h (--help) for help",
        version=lettuce.version)
    parser.add_option("-v", "--verbosity",
                      dest="verbosity",
                      default=3,
                      help='The verbosity level')
    parser.add_option("--no-color",
                      action="store_true",
                      dest="no_color",
                      default=False,
                      help="Don't colorize the command output.")
    parser.add_option("-s", "--scenarios",
                      dest="scenarios",
                      default=None,
                      help='Comma separated list of scenarios to run')
    parser.add_option("-t", "--tag",
                      dest="tags",
                      default=None,
                      action='append',
                      help='Tells lettuce to run the specified tags only; '
                           'can be used multiple times to define more tags'
                           '(prefixing tags with "-" will exclude them and '
                           'prefixing with "~" will match approximate words)')
    parser.add_option("-r", "--random",
                      dest="random",
                      action="store_true",
                      default=False,
                      help="Run scenarios in a more random order to avoid interference")
    parser.add_option("--root-dir",
                      dest="root_dir",
                      default="/",
                      type="string",
                      help="Tells lettuce not to search for features/steps "
                           " above this directory.")
    parser.add_option("--with-xunit",
                      dest="enable_xunit",
                      action="store_true",
                      default=False,
                      help='Output JUnit XML test results to a file')
    parser.add_option("--xunit-file",
                      dest="xunit_file",
                      default=None,
                      type="string",
                      help='Write JUnit XML to this file. Defaults to '
                           'lettucetests.xml')
    parser.add_option("--with-subunit",
                      dest="enable_subunit",
                      action="store_true",
                      default=False,
                      help='Output Subunit test results to a file')
    parser.add_option("--subunit-file",
                      dest="subunit_filename",
                      default=None,
                      help='Write Subunit data to this file. Defaults to '
                           'subunit.bin')
    parser.add_option("--failfast",
                      dest="failfast",
                      default=False,
                      action="store_true",
                      help='Stop running in the first failure')
    parser.add_option("--pdb",
                      dest="auto_pdb",
                      default=False,
                      action="store_true",
                      help='Launches an interactive debugger upon error')
    return parser


if __name__ == '__main__':
    main()
