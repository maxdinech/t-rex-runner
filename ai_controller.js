


(function() {
  'use strict';

  function AIController() {

    // singleton
    if (this.instance_)
      return this.instance_;

    this.runner = undefined;
    this.websocket = undefined;

    this.websocket

      return this;
  }

  window['AIController'] = AIController;

  AIController.prototype = {

    init: function(runner, websocket_url) {
      this.runner = runner;
      this.websocket = new WebSocket(websocket_url);
      this.initWebSocket();

      this.infectRunner();
    },

    initWebSocket: function() {
      this.websocket.onopen = function() {
        console.log("[WebSocket] connection OK");
        this.sendMsg({
          type: 'welcome',
        });
        this.sendDatas([
            {key: 'speed',    value: 6},
            {key: 'obs_dist', value: 600},
            {key: 'obs_size', value: 20},
            {key: 'passed',   value: 0},
            {key: 'score',    value: 0},
            {key: 'crashed',  value: false},
        ]);
      }.bind(this)

      this.websocket.onerror = function(error) {
        console.log("[WebSocket]", error);
        alert("WebSocket error, AI communication closed");
      }.bind(this)

      this.websocket.onmessage = function(raw_msg) {
        console.log("[WebSocket] Receive message from AI");
        msg = JSON.parse(raw_msg)
          switch (msg.type) {
            case 'action':
              doAction(msg.content);
              break;

            default:
              console.log("[WebSocket] Bad message", raw_msg);
              break;
          }
      }
    },

    doAction: function(action_type) {
      switch (action_type) {
        case 'jump':
          this.actionTRexJump();
          break;
      }
    },

    sendData: function(key, value) {
      this.sendMsg({
        type: 'data',
        content: {
          key: key,
          value: value,
        },
      })
    },

    sendDatas: function(keys_values) {
      this.sendMsg({
        type: 'datas',
        content: keys_values,
      })
    },

    sendMsg: function(msg) {
      if (this.runner === undefined || this.websocket === undefined) {
        console.log("Error: Trying to send data when AIController not initialized..");
        return;
      }
      this.websocket.send(JSON.stringify(msg));
    },

    actionTRexJump: function() {
      var event = new Event(keydown ? 'keydown' : 'keyup');
      event.keyCode = 32;
      event.which = event.keyCode;
      event.altKey = false;
      event.ctrlKey = true;
      event.shiftKey = false;
      event.metaKey = false;
      this.runner.onKeyDown(event);
      this.runner.onKeyUp(event);
    },

    infectRunner: function() {
      if (this.runner.infected_)
        return;
      runner.infected_ = true;
      var ai = this;



      runner.update = function() {
        Runner.prototype.update.call(runner);
        ai.sendData('data', this.currentSpeed);
      }
    }

  }
})();

new AIController().init(Runner(), "ws://localhost:4242");

//

// vim:set et sw=2:
