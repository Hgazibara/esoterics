# About

A collection of Python interpreters for various esoteric programming languages.

## Currently implemented

- Brainfuck
- Befunge-93

## Examples

### Brainfuck

```
import esoterics.brainfuck
import esoterics.input

code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
user_input = esoterics.input.PredefinedInput([])

# Will produce 'Hello World!'
esoterics.brainfuck.run(code, user_input)

```

### Befunge-93

```
import esoterics.befunge

code = '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'

# Output must be the same as input code
esoterics.befunge.run(code)
```