### Choose font: Digital-7
### Background & foreground

### import libraries:
```python
from tkinter import*
from tkinter.ttk import*
from time import strftime
```
### Program Counter:
```python
def clock():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)   
    label.after(1000, clock)
```
