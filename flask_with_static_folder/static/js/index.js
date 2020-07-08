const video = document.getElementById('video');

var socket = io.connect('http://127.0.0.1:5000');
socket.on( 'connect', function() {console.log("SOCKET CONNECTED") } )

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
Promise.all([
  faceapi.loadFaceLandmarkModel("http://127.0.0.1:5000/static/models/"),
  faceapi.loadFaceRecognitionModel("http://127.0.0.1:5000/static/models/"),
  faceapi.loadTinyFaceDetectorModel("http://127.0.0.1:5000/static/models/"),
  faceapi.loadFaceLandmarkModel("http://127.0.0.1:5000/static/models/"),
  faceapi.loadFaceLandmarkTinyModel("http://127.0.0.1:5000/static/models/"),
  faceapi.loadFaceRecognitionModel("http://127.0.0.1:5000/static/models/")
]).then(startVideo).catch(err => console.error(err));

function startVideo() {
  console.log("access")
  navigator.getUserMedia( {video: {} }, stream => video.srcObject = stream, err => console.error(err) )
}

video.addEventListener('play', () =>
{
  const canvas = faceapi.createCanvasFromMedia(video);
  document.body.append(canvas);
  const displaySize = { width: video.width, height: video.height };
  faceapi.matchDimensions(canvas, displaySize);

  setInterval(async () =>
  {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks();
    
    var play_check = socket.emit( 'my event', {data: detections})
    if(play_check === "PLAY")
    {
        var sound = new Audio();
        sound.src = 'song.mp3';
        sound.play();
        console.log("INSIDE IF CONDITION")
    }
    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
    faceapi.draw.drawDetections(canvas, resizedDetections);
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);

  }, 100)
})
