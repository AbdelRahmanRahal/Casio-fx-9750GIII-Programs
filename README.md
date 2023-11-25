# Casio fx-9750GIII Programs
A collection of Python programs for Casio fx-9750GIII (and fx-9860GIII, and probably others that I can't test) written by me (mostly).

# CMPLTSQR
Python program for Casio fx-9750GIII (and fx-9860GIII, and probably others that I can't test) to complete the square for standard quadratic expressions.

The main code algorithm is not mine. It belongs to [nokko](https://codereview.stackexchange.com/users/181948/nokko), taken from [this post](https://codereview.stackexchange.com/questions/232625/quadratic-complete-the-square-solver-in-python-3). I just took it and edited to fit Casio's MicroPython.

## How to Use
First, load the script from your calculator's Python section. You will be greeted with some brief instructions on how to use this script. Feel free to read them, or just read this section.

Next, input each term of your quadratic equation **seperated by spaces instead of the additions signs**. Make sure they are in standard form like so:
$$ax^2 + bx + c = 0$$
For example, let's say you want to complete the square for $x^2 + 6x + 41 = 0$, you will then enter the following:

`> 1x**2 6x 41`

This should output the following:
```text
Working with:
1x**2 + 6x + 41

Result is:
1.0(x + (3.0))^2 + (32.0)
```

If you want to enter negative terms, make sure to still include the spaces.
For example, for $x^2 - 6x - 16 = 0$, you will write it like the following:

`> 1x**2 -6x -16`

<br>

> [!IMPORTANT]
> Make sure to always write $x^2$ as `x**2` and not `x^2`. You also have to specify the coefficient of all terms, even if they are 1. So, your final term should look like this `1x**2`.
