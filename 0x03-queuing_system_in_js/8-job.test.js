import {createPushNotificationsJobs} from './8-jobs.js'

queue = require('kue').createQueue();

const j = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 2 to verify your account'
  },
  {
    phoneNumber: '4153518782',
    message: 'This is the code 3 to verify your account'
  }
]
before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

it('does something cool', function() {
  createPushNotificationsJobs(j, queue)
  queue.createJob('myJob', { foo: 'bar' }).save();
  queue.createJob('anotherJob', { baz: 'bip' }).save();
  expect(queue.testMode.jobs.length).to.equal(3);
  expect(queue.testMode.jobs[0].type).to.equal('que');
  expect(queue.testMode.jobs[0].data).to.eql({
    phoneNumber: '4153518780',
    message: 'This is the code 1 to verify your account'
  });
  expect(queue.testMode.jobs[0].data).to.eql({
    phoneNumber: '4153518781',
    message: 'This is the code 2 to verify your account'
  });
  expect(queue.testMode.jobs[0].data).to.eql({
    phoneNumber: '4153518782',
    message: 'This is the code 3 to verify your account'
  });
});


