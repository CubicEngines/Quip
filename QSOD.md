# QuipScript Official Documentation
## QSOD

> It is important to mention that the QSOD uses the official formatting guide, QSFG.
> Using it can help a lot. Make sure to use QSFG 5 as it helps the standard code
> exchange.

### 1. Attachments

Elements can be attached using the `attach` keyword. Attachment initializes all the
variables for the object and recognizes that it is a script for that object. For this
same reason, it can only be used once as shown.

```
attach example
```

### 1.1. Attachment Variables

The variables that come with an object can be used with the object name. It would be
a detail of the object and can come with many details. It will always have 3 universal
details, which are `x`, `y`, and `z`. Their usages are used as shown.

```
attach example

func(example.x, example.y, example.z);
```

### 1.1.1. Attachment Variables Camera

The camera has just the universal detail variables, `x`, `y`, and `z`. The camera also
has a detail function `rotate`, which is used to set the orientation of the camera,
`on`, which is to turn the camera on and all other cameras off, and `update`, which
updates the camera. The following would be a camera movement program.

```
attach camera
get key

camera.on()
var x = camera.x;
var y = camera.y;
var z = camera.z;

var speed = 5;

on tick {
    if key.left == 1 {
        x -= speed;
    }
    
    if key.right == 1 {
        x += speed;
    }
    
    if key.up == 1 {
        z += speed;
    }
    
    if key.down {
        z -= speed;
    }
    
    camera.rotate(x, y, z);
    camera.update();
}
```

### 1.1.2 Attachment Variables Object

Objects have the universal variables, `x`, `y`, and `z`, as well as custom details
like `width`, `height`, `depth`, `color`
