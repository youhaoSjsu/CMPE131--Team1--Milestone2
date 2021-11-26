# Pomodoro timer

### HTML file

We use JavaScript to display a live clock, and a countdown timer

Countdown timer

```
{% extends "base.html" %} {% block content %}

<body class="text-center">
  <h1 style="color: black;"><strong> Pomodoro </strong></h1>
  <div id="txt" style="color: black; margin-bottom: 15px;"></div>

    <strong style="color: black;">Set Timer (in minutes):</strong> <input id="userInput" type="number" value="0" />
  </p>
  <button onclick="start()">Start</button>
  <button onclick="stop()">Stop</button>
  <p style="color: black;" id="timer1">0000</p>
  <audio id="timeout_audio" src ="static/beepbeep.mp3" autoplay ="False"></audio>
  <script>
    //countdown timer
    const timeoutAudio = document.getElementById("timeout_audio");
    var countdownTimer;
    var timer = document.getElementById("userInput");
    var myTimer;


    function start() {
      countdownTimer = setInterval(startTimer, 1000);
      document.getElementById("timer1").innerHTML = timer.value;
      myTimer = timer.value * 60;
    }
    // timeoutAudio.src = "beepbeep.mp3";
    timeoutAudio.load();

    function startTimer() {
      myTimer--;
      document.getElementById("timer1").innerHTML = myTimer;
      if (myTimer == -1) {
        stop();
        document.getElementById("timer1").innerHTML = "0";
        alert ('Time is up!');
      }
    }
    function stop() {
      clearInterval(countdownTimer);
      timeoutAudio.play();
    }
```

Display a live clock

```
    function startTime() {
      const today = new Date();
      let h = today.getHours();
      let m = today.getMinutes();
      let s = today.getSeconds();
      m = checkTime(m);
      s = checkTime(s);
      document.getElementById("txt").innerHTML = h + ":" + m + ":" + s;
      setTimeout(startTime, 1000);
    }

    function checkTime(i) {
      if (i < 10) {
        i = "0" + i;
      }
      return i;
    }
    setInterval(function () {
      startTime();
    }, 500);
  </script>

  {% endblock %}
</body>
```

### Timer function

```python
@app_Obj.route('/timer', methods = ['GET', 'POST'])
def pomodoro ():
    form = pomorodoTimerForm()
    title = 'Start a Timer'
    if request.method == 'POST':
        try:
            study_time = (request.form ["study_time"])
            #break_time = (request.form ["break_time"])
            timer (int(study_time))
            return redirect ("/timer")
        except:
            return flash ('Fail to load timer')
    else:
        return render_template ("timer.html", form = form,title=title)

def timer (t):
    # t = 25*60
    while t:
        mins, secs = divmod (t, 60)
        timer = '{:02d}: {:02d}'.format (mins, secs)
        print (timer, end = "\r")
        time.sleep(1)
        t -=1
    pyttsx3.speak ("beep beep beep beep time to work")
    return t
```

### Pomodoro form

```python
class pomorodoTimerForm (FlaskForm):
    study_time = IntegerField('Study Time', validators = [DataRequired()])
    # break_time = IntegerField('Break Time', validators = [DataRequired()])
    start_button = SubmitField('Start')
    # reset_button = SubmitField('Reset')
```
