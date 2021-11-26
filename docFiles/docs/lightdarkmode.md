# Dark and Light function

### JavaScript

```
<a class="navbar-brand btn btn-dark" type="button" style="width: auto;color: whitesmoke; background-color: #000;" onclick="replaceColors_Dark()" id='DarkModeButton'>Dark Mode</a>
            <script>
              function replaceColors_Dark() {
                document.getElementById("DarkModeButton").style.display = 'none'
                document.getElementById("LightModeButton").style.display = 'block'
                document.body.outerHTML = document.body.outerHTML.replace(/white/g, '#212121').replace(/black/g,'white')
              }
            </script>
            <a class="navbar-brand btn btn-light" type="button" style="width: auto;color: darkblue; display: none;" onclick="replaceColors_Light()" id='LightModeButton'>Light Mode</a>
            <script>
              function replaceColors_Light() {
                document.getElementById("DarkModeButton").style.display = 'block'
                document.getElementById("LightModeButton").style.display = 'none'
                document.body.outerHTML = document.body.outerHTML.replace(/white/g, "black").replace(/#212121/g, "white")
              }
            </script>
```
