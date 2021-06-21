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
    example();
}
```

### 5

Use tabs instead of spaces and use four spaces
width for your tabs. Editor tab to spaces setting
should be off.
