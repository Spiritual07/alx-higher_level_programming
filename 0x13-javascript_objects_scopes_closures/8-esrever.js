#!/usr/bin/node

exports.esrever = function (list) {
  let leftIndex = 0;
  let rightIndex = list.length - 1;
  while (leftIndex < rightIndex) {
    const temp = list[leftIndex];
    list[leftIndex] = list[rightIndex];
    list[rightIndex] = temp;

    leftIndex++;
    rightIndex--;
  }
  return list;
};
