# Break Alert page

### Break Alert function

We added a piece of Javascript inside home.html, view_flashcard.html, and flashcard.html.

```python
<script>
        setTimeout(function confirmAction() {
          let confirmAction = confirm(
            "You've studied for one hour. Do you want to take a break?"
          );
          if (confirmAction) {
            alert("Enjoy your break!");
          } else {
            alert("Have a good study!");
          }
        }, 3600000);
</script>
```

Exlaination, we set timeout one hour, so every one hour, there will be a pop-up message ask users if they want to have a break.
