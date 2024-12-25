import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 640
    height: 300
    color: "lightblue"

    Text {
        id: textElement
        text: "Texto do QML"
        anchors.centerIn: parent
        font.pixelSize: 32

        MouseArea {
            anchors.fill: parent
            onClicked: console.log("Button clicked!")
        }
    }
}
