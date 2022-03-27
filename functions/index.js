const admin = require('firebase-admin');
const functions = require("firebase-functions");
const firestore = admin.firestore();

exports.helloJacobs = functions.https.onRequest((request, response) => {
  functions.logger.info("Hello Jacobs!", {structuredData: true});
  response.send("Welcome to Firebase jam!");
});

exports.sendMissingPostCreationNotification = functions
  .firestore
  .document("/missing_posts")
  .onCreate((snapshot, context) => {
    const post = snapshot.data();
    const latitude = post['latitude'];
    const longitude = post['longitude'];
    const ten_mile_lat = 0.144927536231884;
    const ten_mile_lon = 0.181818181818182;
    users = db.collection('users')
      // TODO: implement query to get nearby users based on post's lat/long

      .where()
      .get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          // TODO: send notification to said users

        })
      })
      .catch((err) => {

      })

    return 1;
});
