
Write a program in Python language for encoding and decoding a text with the Morse alphabet. The Morse alphabet is a code that assigns, to each letter of the alphabet, number or punctuation symbol, a variable-length code, consisting of dots and dashes.

The conversion table is contained in the file `morse.txt`, of which the first lines are represented:

    A .-
    B -...
    C -.-.
    D -..
    E .
    F ..-.
    G --.
    (etc...)

On each line, the first character represents the alphanumeric symbol, followed by the corresponding sequence of dots and dashes, separated by a space.

The program reads from the file `command.txt` the sequence of translations to be performed. The file consists of multiple lines, and each line consists of two fields separated by a space:

- the first field contains `c` if it is necessary to **c**ode (from text to Morse), or contains `d` if it is necessary to **d**ecode (from Morse to text) a message
- the second field contains the name of the file to encode/decode. This file will contain only one line of text.

The program must then output the translation (encoding/decoding) of the various requested files.

## Notes

The program, in the case of encoding, must skip the encoding of all characters not present in the file `morse.txt`, and must not distinguish between lowercase and uppercase characters.

The program, in the case of encoding, must separate with a space the Morse symbols printed as a result.

In the case of decoding, assume that the text to be decoded consists of Morse symbols separated by a space.
Any Morse symbols not recognized should be ignored.

Assume that there are no formatting errors in the files.

## Execution Example

Suppose that the file `command.txt` contains:

    c text.txt
    d code.txt

and that the file *text.txt* contains:

    Hi! Welcome to my GITHUB!

and the file *code.txt* contains:

    .... .. -.-.-- / .-- . .-.. -.-. --- -- . / - --- / -- -.-- / --. .. - .... ..- -... -.-.--

The output printed will be:

    Encoding of file text.txt:
    .... .. .-- . .-.. -.-. --- -- . - --- -- -.-- --. .. - .... ..- -...
    Decoding of file codice.txt:
    HIWELCOMETOMYGITHUB

