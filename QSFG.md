# QuipScript Formatting Guide
## QSFG

### 1

Even if double and single quotes are the same,
use double for your main programs and single for
test ones.

### 2

Add comments four spaces after the line and more
if making a cluster as shown.

```
example();    // comment
```

```
example();         // comment
example(param);    // another comment
```

### 3

Don't use comments on closing brace lines.

### 4

Use opening braces on the starting line and end
braces on a separate one as shown.

```
if example == 0 {
    func();
}
```

### 5

Use tabs instead of spaces and use four spaces
width for your tabs. Editor tab to spaces setting
should be off.

### 6

Character spacing should be ideal and proper as
shown.

```
example(1, 2, 3);
var x = 0;
```

### 7

Line spacing varies. One line should be present
between events. One line should be between your
`attach` or `get` and your code. Two lines should
be between comment clusters and code. This is as
shown.

```
on tick {
    func(0);
}

on change example {
    func(1);
}
```

```
attach example
get random

on tick {
    func();
}
```

```
attach example
get random


// attaches to example
// gets random
// calls func on tick


on tick {
    func();
}
```

### 8

Use `link` only for singular code. Don't use
it as a mix of one or the other.
