import QtQuick 2.15
import QtQuick.Controls 2.15

ScrollView {
    width: 500
    height: 500

    ListView {
        model: 20
        delegate: ItemDelegate {
            text: "Item " + index

            required property int index
        }
    }
}
