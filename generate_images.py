import turtle
from subprocess import run, DEVNULL
from os import makedirs, path


def save(screen: turtle.Screen, directory: str = 'imgs', file_name: str = 'spider') -> None:
    """
    Save the turtle screen as a postscript file.
    :param screen: The turtle screen to save images of.
    :param directory: The path to the directory where all the files should be saved to.
    :param file_name: The base name of all the files (without a file extension).
    """

    makedirs(directory, exist_ok=True)
    file_location = path.join(directory, file_name)

    # Create PostScript file to generate the rest of the files from.
    canvas = screen.getcanvas()
    canvas.postscript(file=file_location + '.ps')

    # We can only generate SVG or PNG files from PostScript files with Inkscape.
    if inkscape_exists():
        save_svg(file_location)
        save_png(file_location)
    else:
        print(
            'The command `inkscape` does not exist on your PATH. You probably need to install Inkscape.',
            'As a result, no SVG or PNG files will be generated.',
            sep='\n',
        )


def inkscape_exists() -> bool:
    """Returns true if inkscape exists on $PATH, and returns false otherwise."""
    return not run(['command', '-v', 'inkscape'], stdout=DEVNULL).returncode


def save_file_type(file_location, file_type: str, additional_options: list) -> None:
    """
    Generate an image from a preexisting PostScript file. Fails if Inkscape is not installed.
    :param file_location: The path to the directory where the PostScript file is and to save files to.
    :param file_type: The file extension of the resulting file. Eg. "svg".
    :param additional_options: Additional options to pass into inkscape.
    """
    run([
        'inkscape', file_location + '.ps',
        '-D',  # Export the entire drawing, ignoring page size.
        *additional_options,
        '-o', '.'.join([file_location, file_type]),
    ], check=True)


def save_svg(file_location) -> None:
    """
    Generate an SVG image from a PostScript file. Fails if Inkscape is not installed.
    :param file_location: Passed to `save_file_type`.
    """
    # `--export-plain-svg` remove Inkscape-specific attributes/properties
    save_file_type(file_location, 'svg', ['--export-plain-svg'])


def save_png(file_location, dimensions: int = None) -> None:
    """
    Generate an PNG image from a PostScript file. Fails if Inkscape is not installed.
    :param file_location: Passed to `save_file_type`.
    :param dimensions: Manually specifies the dimensions of the resulting image.
    """
    dimensions_args = ['-w', str(dimensions), '-h', str(dimensions)] if dimensions else []
    save_file_type(file_location, 'png', dimensions_args)
