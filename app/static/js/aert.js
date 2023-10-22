// class MessageBox {
//     constructor(option) {
//       this.option = option;
      
//       this.msgBoxArea = document.querySelector("#msgbox-area");
      
//       if (this.msgBoxArea === null) {
//         this.msgBoxArea = document.createElement("DIV");
//         this.msgBoxArea.setAttribute("id", "msgbox-area");
//         this.msgBoxArea.classList.add("msgbox-area");
        
//         document.body.appendChild(this.msgBoxArea);
//       }
//     }
    
//     show(msg, callback, closeLabel) {
//       if (msg === "" || msg === undefined || msg === null) {
//         // If the 'msg' parameter is not set, throw an error
        
//         throw "Message is empty or not defined.";
//       }
      
//       if (closeLabel === undefined || closeLabel === null) {
//         // Of the close label is undefined, or if it is null
        
//         closeLabel = "Close";
//       }
      
//       const option = this.option;
  
//       const msgboxBox = document.createElement("DIV");
//       const msgboxContent = document.createElement("DIV");
//       const msgboxCommand = document.createElement("DIV");
//       const msgboxClose = document.createElement("A");
      
//       // Content area of the message box
//       msgboxContent.classList.add("msgbox-content");
//       msgboxContent.innerText = msg;
      
//       // Command box or the button container
//       msgboxCommand.classList.add("msgbox-command");
      
//       // Close button of the message box
//       msgboxClose.classList.add("msgbox-close");
//       msgboxClose.setAttribute("href", "#");
//       msgboxClose.innerText = closeLabel;
      
//       // Container of the Message Box element
//       msgboxBox.classList.add("msgbox-box");
//       msgboxBox.appendChild(msgboxContent);
  
//       if (option.hideCloseButton === false
//           || option.hideCloseButton === undefined) {
//         // If the hideCloseButton flag is false, or if it is undefined
        
//         // Append the close button to the container
//         msgboxCommand.appendChild(msgboxClose);
//         msgboxBox.appendChild(msgboxCommand);
//       }
  
//       this.msgBoxArea.appendChild(msgboxBox);
      
//       msgboxClose.onclick = (evt) => {
//         evt.preventDefault();
        
//         if (msgboxBox.classList.contains("msgbox-box-hide")) {
//           return;
//         }
        
//         clearTimeout(this.msgboxTimeout);
        
//         this.msgboxTimeout = null;
  
//         this.hide(msgboxBox, callback);
//       };
  
//       if (option.closeTime > 0) {
//         this.msgboxTimeout = setTimeout(() => {
//           this.hide(msgboxBox, callback);
//         }, option.closeTime);
//       }
//     }
    
//     hideMessageBox(msgboxBox) {
//       return new Promise(resolve => {
//         msgboxBox.ontransitionend = () => {
//           resolve();
//         };
//       });
//     }
    
//     async hide(msgboxBox, callback) {
//       if (msgboxBox !== null) {
//         // If the Message Box is not yet closed
        
//         msgboxBox.classList.add("msgbox-box-hide");
//       }
      
//       await this.hideMessageBox(msgboxBox);
      
//       this.msgBoxArea.removeChild(msgboxBox);
  
//       clearTimeout(this.msgboxTimeout);
      
//       if (typeof callback === "function") {
//         // If the callback parameter is a function
  
//         callback();
//       }
//     }
//   }
  
//   const msgboxShowMessage = document.querySelector("#msgboxShowMessage");
//   const msgboxHiddenClose = document.querySelector("#msgboxHiddenClose");
  
//   // Creation of Message Box class, and the sample usage
//   const msgbox = new MessageBox({
//     closeTime: 10000,
//     hideCloseButton: false
//   });
//   const msgboxPersistent = new MessageBox({
//     closeTime: 0
//   });
//   const msgboxNoClose = new MessageBox({
//     closeTime: 5000,
//     hideCloseButton: true
//   });
  
//   document.querySelector("#msgboxPersistent").addEventListener("click", () => {
//     msgboxPersistent.show("salom bizning suni ong loihamizga hush kelibsiz ayni damda unda hatoliklar bor bolishi mumkin sidan bu hatoliklar uchun uzur so`raymiz bizning AI modelimiz hozircha faqat ingliz tilida suhbatlasha oladi");
//   });
  
//   msgboxShowMessage.addEventListener("click", () => {
//     msgbox.show("salom bizning suni ong loihamizga hush kelibsiz ayni damda unda hatoliklar bor bolishi mumkin sidan bu hatoliklar uchun uzur so`raymiz bizning AI modelimiz hozircha faqat ingliz tilida suhbatlasha oladi.", null);
//   });
  
// //   msgboxHiddenClose.addEventListener("click", () => {
// //     msgboxNoClose.show("salom bizning suni ong loihamizga hush kelibsiz ayni damda unda hatoliklar bor bolishi mumkin sidan bu hatoliklar uchun uzur so`raymiz bizning AI modelimiz hozircha faqat ingliz tilida suhbatlasha oladi");
// //   });
  
// //   // Show the message at the beginning
// //   msgboxPersistent.show(
// //     "",
// //     () => {
// //       console.log("I am the callback! Of course, you may add various javaScript codes to make the callback function colourful.");
// //     },
// //     "Has callback"
// //   );

class MessageBox {
    constructor(option) {
      this.option = option;
      this.msgBoxArea = document.querySelector("#msgbox-area");

      if (this.msgBoxArea === null) {
        this.msgBoxArea = document.createElement("DIV");
        this.msgBoxArea.setAttribute("id", "msgbox-area");
        this.msgBoxArea.classList.add("msgbox-area");
        document.body.appendChild(this.msgBoxArea);
      }
    }

    show(msg, callback, closeLabel) {
      if (msg === "" || msg === undefined || msg === null) {
        throw "Xabar bo'sh yoki aniqlanmagan.";
      }

      if (closeLabel === undefined || closeLabel === null) {
        closeLabel = "Yopish";
      }

      const option = this.option;

      const msgboxBox = document.createElement("DIV");
      const msgboxContent = document.createElement("DIV");
      const msgboxCommand = document.createElement("DIV");
      const msgboxClose = document.createElement("A");

      msgboxContent.classList.add("msgbox-content");
      msgboxContent.innerText = msg;

      msgboxCommand.classList.add("msgbox-command");

      msgboxClose.classList.add("msgbox-close");
      msgboxClose.setAttribute("href", "#");
      msgboxClose.innerText = closeLabel;

      msgboxBox.classList.add("msgbox-box");
      msgboxBox.appendChild(msgboxContent);

      if (option.hideCloseButton === false || option.hideCloseButton === undefined) {
        msgboxCommand.appendChild(msgboxClose);
        msgboxBox.appendChild(msgboxCommand);
      }

      this.msgBoxArea.appendChild(msgboxBox);

      msgboxClose.onclick = (evt) => {
        evt.preventDefault();

        if (msgboxBox.classList.contains("msgbox-box-hide")) {
          return;
        }

        clearTimeout(this.msgboxTimeout);
        this.msgboxTimeout = null;

        this.hide(msgboxBox, callback);
      };

      if (option.closeTime > 0) {
        this.msgboxTimeout = setTimeout(() => {
          this.hide(msgboxBox, callback);
        }, option.closeTime);
      }
    }

    hideMessageBox(msgboxBox) {
      return new Promise((resolve) => {
        msgboxBox.ontransitionend = () => {
          resolve();
        };
      });
    }

    async hide(msgboxBox, callback) {
      if (msgboxBox !== null) {
        msgboxBox.classList.add("msgbox-box-hide");
      }

      await this.hideMessageBox(msgboxBox);

      this.msgBoxArea.removeChild(msgboxBox);
      clearTimeout(this.msgboxTimeout);

      if (typeof callback === "function") {
        callback();
      }
    }
  }

  const msgbox = new MessageBox({
    closeTime: 20000,
    hideCloseButton: false,
  });

  // Xabarni ko'rsatish


  // Automatik chiqish uchun 3 sekunddan so'ng
  setTimeout(() => {
    msgbox.show(
      "salom bizning suni ong loihamizga hush kelibsiz ayni damda unda hatoliklar bor bolishi mumkin sizdan bu hatoliklar uchun uzur soraymiz bizning AI modelimiz hozircha faqat ingliz tilida suhbatlasha oladi.",
      null
    );
  }, 3000);