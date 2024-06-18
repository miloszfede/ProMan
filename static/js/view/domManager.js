// import {changeBoardsNameWindow} from "./htmlFactory";

export let domManager = {
    addChild(parentIdentifier, childContent) {
        const parent = document.querySelector(parentIdentifier);
        if (parent) {
            parent.insertAdjacentHTML("beforeend", childContent);
        } else {
            console.error("could not find such html element: " + parentIdentifier);
        }
    },
    addEventListener(parentIdentifier, eventType, eventHandler) {
        const parent = document.querySelector(parentIdentifier);
        if (parent) {
            parent.addEventListener(eventType, eventHandler);
        } else {
            console.error("could not find such html element: " + parentIdentifier);
        }
    },
};

export function changeBoardName() {

    let boardTitles = document.querySelectorAll('.board-title');

    boardTitles.forEach(boardTitle => {

        boardTitle.addEventListener('click', alert('test'));

    });



}