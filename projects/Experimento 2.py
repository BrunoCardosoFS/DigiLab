from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtSvgWidgets import QSvgWidget


svg_base = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="a">
            <stop style="stop-color:#0d69ff;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#0055e3;stop-opacity:1" offset=".525"/>
            <stop style="stop-color:#005bef;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="b" x1="249.135" y1="523.474" x2="752.557" y2="523.474" gradientUnits="userSpaceOnUse"/>
    </defs>
    <path style="fill:#000;fill-opacity:1;stroke-linecap:round;paint-order:markers fill stroke" d="M7.347 56.791a4.5 4.5 0 0 0-4.5 4.5v712.203a4.5 4.5 0 0 0 4.497 4.5l20.343.037c.732.001 1.395-.212 2.006-.521v34.504A7.968 7.968 0 0 0 37.68 820h274.076a7.968 7.968 0 0 0 7.986-7.986V778.03h39.338a4.5 4.5 0 0 0 0-9h-39.338V735.05a7.968 7.968 0 0 0-7.986-7.987H245.92v-108.23h113.16a4.5 4.5 0 0 0 0-9H241.42a4.5 4.5 0 0 0-4.5 4.5v112.73h-53.506v-334.04H359.08a4.5 4.5 0 0 0 0-9H178.914a4.5 4.5 0 0 0-4.5 4.5v338.54h-60.322V170.114H359.08a4.5 4.5 0 0 0 0-9H109.592a4.5 4.5 0 0 0-4.5 4.5v561.45H37.68a7.968 7.968 0 0 0-7.987 7.986v34.504c-.608-.308-1.268-.521-1.996-.522l-15.85-.033V65.791H248.62a4.5 4.5 0 0 0 0-9z"/>
    <g transform="translate(-362.197 -135.55)">
        <rect style="fill:#000;fill-opacity:1;stroke:none;stroke-width:3.87274;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="125.46" height="39.906" x="217.28" y="95.567" ry="6.129" transform="translate(393.535 81.321)"/>
        <circle style="fill:#35e100;fill-opacity:1;stroke:#0d0d0d;stroke-width:.5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" cx="706.043" cy="197.408" r="4.438"/>
    </g>
</svg>
"""

svg_agua = """
<svg width="500" height="720" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="a">
            <stop style="stop-color:#0d69ff;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#0055e3;stop-opacity:1" offset=".525"/>
            <stop style="stop-color:#005bef;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="b" x1="249.135" y1="523.474" x2="752.557" y2="523.474" gradientUnits="userSpaceOnUse"/>
    </defs>
    <g style="display:inline">
        <g style="display:inline">
            <path style="display:inline;fill:url(#b);fill-opacity:1;stroke:none;stroke-width:1;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M249.135 160.321h503.422v726.306H249.135z" transform="matrix(.9932 0 0 .99132 -247.441 -158.93)"/>
        </g>
    </g>
</svg>
"""
svg_agua_open = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="b">
            <stop style="stop-color:#0057e7;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#0048c2;stop-opacity:1" offset=".55"/>
            <stop style="stop-color:#0057e7;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#b" id="c" x1="245.566" y1="504.289" x2="660.158" y2="456.368" gradientUnits="userSpaceOnUse"/>
    </defs>
    <g style="display:inline">
        <path style="display:inline;fill:url(#c);stroke-width:40;stroke-linecap:round;stroke-linejoin:round;paint-order:markers fill stroke" d="M245.73 160.406s15.205.284 31.937 1.09c16.732.805 44.962 15.259 58.812 35.214 13.851 19.956 20.953 46.894 27.241 84.656 6.288 37.762 14.139 104.335 18.218 225.164 4.079 120.828-5.802 377.602-5.802 377.602l279.666 1.027s-10.8-194.792-24.51-313.333c-13.711-118.54-31.523-189.966-62.346-253.733-30.823-63.768-70.547-104.324-102.066-128.81-31.52-24.485-72.286-50.202-117.406-60.634-29.552-6.832-74.875-5.01-74.875-5.01l-29.033-.099Z" transform="translate(122.04 -78.36)"/>
    </g>
</svg>
"""

svg_tanque = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="a">
            <stop style="stop-color:#0d69ff;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#0055e3;stop-opacity:1" offset=".525"/>
            <stop style="stop-color:#005bef;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="b" x1="249.135" y1="523.474" x2="752.557" y2="523.474" gradientUnits="userSpaceOnUse"/>
    </defs>
    <g style="display:inline">
        <path style="display:inline;stroke-linecap:round;stroke-linejoin:round;paint-order:markers fill stroke" d="M237.04 84.443V890.86a7.5 7.5 0 0 0 7.5 7.5h512.612a7.5 7.5 0 0 0 7.5-7.5V126.896h30.903v-5.873H749.652V883.36H252.04V84.443Zm512.612 0V96.99h45.903v-5.873h-30.903v-6.674z" transform="translate(122.04 -78.36)"/>
    </g>
</svg>
"""

svg_sensor_1_on = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <path style="display:inline;fill:#35e100;fill-opacity:1;stroke:#000;stroke-width:.666111;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="m273.955 684.006-15.306-3.57v25.908l15.306-3.57zm-15.306-6.123h-6.61v31.014h6.61z" transform="translate(122.04 -78.36)"/>
</svg>
"""
svg_sensor_2_on = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <path style="display:inline;fill:#35e100;fill-opacity:1;stroke:#000;stroke-width:.666111;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="m273.955 458.865-15.306-3.57v25.907l15.306-3.57zm-15.306-6.124h-6.61v31.014h6.61z" transform="translate(122.04 -78.36)"/>
</svg>
"""
svg_sensor_3_on = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <path style="display:inline;fill:#35e100;fill-opacity:1;stroke:#000;stroke-width:.666111;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="m273.955 233.723-15.306-3.57v25.908l15.306-3.57zM258.65 227.6h-6.61v31.014h6.61z" transform="translate(122.04 -78.36)"/>
</svg>
"""

svg_sensor_1_off = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#5e5e5e;fill-opacity:1;stroke:#000;stroke-width:.666111;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="m273.955 684.006-15.306-3.57v25.908l15.306-3.57zm-15.306-6.123h-6.61v31.014h6.61z" transform="translate(122.04 -78.36)"/>
    </g>
</svg>
"""
svg_sensor_2_off = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#5e5e5e;fill-opacity:1;stroke:#000;stroke-width:.666111;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="m273.955 458.865-15.306-3.57v25.907l15.306-3.57zm-15.306-6.124h-6.61v31.014h6.61z" transform="translate(122.04 -78.36)"/>
    </g>
</svg>
"""
svg_sensor_3_off = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#5e5e5e;fill-opacity:1;stroke:#000;stroke-width:.666111;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="m273.955 233.723-15.306-3.57v25.908l15.306-3.57zM258.65 227.6h-6.61v31.014h6.61z" transform="translate(122.04 -78.36)"/>
    </g>
</svg>
"""

svg_sensor_1_q_on = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#35e100;stroke-linecap:round;paint-order:markers fill stroke" d="M252.04 677.883v2.26l.982.91.336.146 2.676 1.164 2.615-3.781v-.7zm6.836 2.605-1.654 2.39 2.582 1.122.127.057.091.101 4.217 4.695 1.733 1.762.543-1.732-.006-.002 1.863-6.178zm-6.836 1.385v7.754l1.887-.711-1.354-6.57-.01.011zm1.934.977 1.252 6.08 12.527 5.3-8.584-9.123zm15.634.142-2.664 8.615.924.971 6.088-3.922v-4.65zm-15.054 7.041-2.514.947v10.782l9.518-5.448 3.197-2.261-2.569-1.153-.002.008-3.898-1.47-.273-.078-.157-.082zm19.402.367-3.096 2.084-.93.713 4.026 2.508zm-5.78 3.225-.859 9.264.909 1.22 5.73-1.336V697.2l-2.924-1.822zm-2.331.92-5.082 3.69-4.452 2.544 3.954 5.188 6.615-1.543-.723-.973-.14-.191.017-.239.918-8.107zm-10.645 6.87-3.16 1.808v5.673h6.61v-2.552l.261-.06z" transform="translate(122.04 -78.36)"/>
        <path style="display:inline;stroke-linecap:round;paint-order:markers fill stroke" d="M251.705 677.55v31.68h7.277v-2.623l15.307-3.57v-19.295l-15.307-3.57v-2.621zm.668.667h5.943v30.347h-5.943zm6.61 2.638 14.64 3.415v18.24l-14.64 3.414z" transform="translate(122.04 -78.36)"/>
    </g>
</svg>
"""
svg_sensor_2_q_on = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#35e100;stroke-linecap:round;paint-order:markers fill stroke" d="M252.04 677.883v2.26l.982.91.336.146 2.676 1.164 2.615-3.781v-.7zm6.836 2.605-1.654 2.39 2.582 1.122.127.057.091.101 4.217 4.695 1.733 1.762.543-1.732-.006-.002 1.863-6.178zm-6.836 1.385v7.754l1.887-.711-1.354-6.57-.01.011zm1.934.977 1.252 6.08 12.527 5.3-8.584-9.123zm15.634.142-2.664 8.615.924.971 6.088-3.922v-4.65zm-15.054 7.041-2.514.947v10.782l9.518-5.448 3.197-2.261-2.569-1.153-.002.008-3.898-1.47-.273-.078-.157-.082zm19.402.367-3.096 2.084-.93.713 4.026 2.508zm-5.78 3.225-.859 9.264.909 1.22 5.73-1.336V697.2l-2.924-1.822zm-2.331.92-5.082 3.69-4.452 2.544 3.954 5.188 6.615-1.543-.723-.973-.14-.191.017-.239.918-8.107zm-10.645 6.87-3.16 1.808v5.673h6.61v-2.552l.261-.06z" transform="translate(122.04 -303.5)"/>
        <path style="display:inline;stroke-linecap:round;paint-order:markers fill stroke" d="M251.705 677.55v31.68h7.277v-2.623l15.307-3.57v-19.295l-15.307-3.57v-2.621zm.668.667h5.943v30.347h-5.943zm6.61 2.638 14.64 3.415v18.24l-14.64 3.414z" transform="translate(122.04 -303.5)"/>
    </g>
</svg>
"""
svg_sensor_3_q_on = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#35e100;stroke-linecap:round;paint-order:markers fill stroke" d="M252.04 677.883v2.26l.982.91.336.146 2.676 1.164 2.615-3.781v-.7zm6.836 2.605-1.654 2.39 2.582 1.122.127.057.091.101 4.217 4.695 1.733 1.762.543-1.732-.006-.002 1.863-6.178zm-6.836 1.385v7.754l1.887-.711-1.354-6.57-.01.011zm1.934.977 1.252 6.08 12.527 5.3-8.584-9.123zm15.634.142-2.664 8.615.924.971 6.088-3.922v-4.65zm-15.054 7.041-2.514.947v10.782l9.518-5.448 3.197-2.261-2.569-1.153-.002.008-3.898-1.47-.273-.078-.157-.082zm19.402.367-3.096 2.084-.93.713 4.026 2.508zm-5.78 3.225-.859 9.264.909 1.22 5.73-1.336V697.2l-2.924-1.822zm-2.331.92-5.082 3.69-4.452 2.544 3.954 5.188 6.615-1.543-.723-.973-.14-.191.017-.239.918-8.107zm-10.645 6.87-3.16 1.808v5.673h6.61v-2.552l.261-.06z" transform="translate(122.04 -528.643)"/>
        <path style="display:inline;stroke-linecap:round;paint-order:markers fill stroke" d="M251.705 677.55v31.68h7.277v-2.623l15.307-3.57v-19.295l-15.307-3.57v-2.621zm.668.667h5.943v30.347h-5.943zm6.61 2.638 14.64 3.415v18.24l-14.64 3.414z" transform="translate(122.04 -528.643)"/>
    </g>
</svg>
"""

svg_sensor_1_q_off = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#5e5e5e;fill-opacity:1;stroke-linecap:round;paint-order:markers fill stroke" d="M252.04 677.883v2.26l.982.91.336.146 2.676 1.164 2.615-3.781v-.7zm6.836 2.605-1.654 2.39 2.582 1.122.127.057.091.101 4.217 4.695 1.733 1.762.543-1.732-.006-.002 1.863-6.178zm-6.836 1.385v7.754l1.887-.711-1.354-6.57-.01.011zm1.934.977 1.252 6.08 12.527 5.3-8.584-9.123zm15.634.142-2.664 8.615.924.971 6.088-3.922v-4.65zm-15.054 7.041-2.514.947v10.782l9.518-5.448 3.197-2.261-2.569-1.153-.002.008-3.898-1.47-.273-.078-.157-.082zm19.402.367-3.096 2.084-.93.713 4.026 2.508zm-5.78 3.225-.859 9.264.909 1.22 5.73-1.336V697.2l-2.924-1.822zm-2.331.92-5.082 3.69-4.452 2.544 3.954 5.188 6.615-1.543-.723-.973-.14-.191.017-.239.918-8.107zm-10.645 6.87-3.16 1.808v5.673h6.61v-2.552l.261-.06z" transform="translate(122.04 -78.36)"/>
        <path style="display:inline;stroke-linecap:round;paint-order:markers fill stroke" d="M251.705 677.55v31.68h7.277v-2.623l15.307-3.57v-19.295l-15.307-3.57v-2.621zm.668.667h5.943v30.347h-5.943zm6.61 2.638 14.64 3.415v18.24l-14.64 3.414z" transform="translate(122.04 -78.36)"/>
    </g>
</svg>
"""
svg_sensor_2_q_off = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#5e5e5e;fill-opacity:1;stroke-linecap:round;paint-order:markers fill stroke" d="M252.04 677.883v2.26l.982.91.336.146 2.676 1.164 2.615-3.781v-.7zm6.836 2.605-1.654 2.39 2.582 1.122.127.057.091.101 4.217 4.695 1.733 1.762.543-1.732-.006-.002 1.863-6.178zm-6.836 1.385v7.754l1.887-.711-1.354-6.57-.01.011zm1.934.977 1.252 6.08 12.527 5.3-8.584-9.123zm15.634.142-2.664 8.615.924.971 6.088-3.922v-4.65zm-15.054 7.041-2.514.947v10.782l9.518-5.448 3.197-2.261-2.569-1.153-.002.008-3.898-1.47-.273-.078-.157-.082zm19.402.367-3.096 2.084-.93.713 4.026 2.508zm-5.78 3.225-.859 9.264.909 1.22 5.73-1.336V697.2l-2.924-1.822zm-2.331.92-5.082 3.69-4.452 2.544 3.954 5.188 6.615-1.543-.723-.973-.14-.191.017-.239.918-8.107zm-10.645 6.87-3.16 1.808v5.673h6.61v-2.552l.261-.06z" transform="translate(122.04 -303.5)"/>
        <path style="display:inline;stroke-linecap:round;paint-order:markers fill stroke" d="M251.705 677.55v31.68h7.277v-2.623l15.307-3.57v-19.295l-15.307-3.57v-2.621zm.668.667h5.943v30.347h-5.943zm6.61 2.638 14.64 3.415v18.24l-14.64 3.414z" transform="translate(122.04 -303.5)"/>
    </g>
</svg>
"""
svg_sensor_3_q_off = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="display:inline;fill:#5e5e5e;fill-opacity:1;stroke-linecap:round;paint-order:markers fill stroke" d="M252.04 677.883v2.26l.982.91.336.146 2.676 1.164 2.615-3.781v-.7zm6.836 2.605-1.654 2.39 2.582 1.122.127.057.091.101 4.217 4.695 1.733 1.762.543-1.732-.006-.002 1.863-6.178zm-6.836 1.385v7.754l1.887-.711-1.354-6.57-.01.011zm1.934.977 1.252 6.08 12.527 5.3-8.584-9.123zm15.634.142-2.664 8.615.924.971 6.088-3.922v-4.65zm-15.054 7.041-2.514.947v10.782l9.518-5.448 3.197-2.261-2.569-1.153-.002.008-3.898-1.47-.273-.078-.157-.082zm19.402.367-3.096 2.084-.93.713 4.026 2.508zm-5.78 3.225-.859 9.264.909 1.22 5.73-1.336V697.2l-2.924-1.822zm-2.331.92-5.082 3.69-4.452 2.544 3.954 5.188 6.615-1.543-.723-.973-.14-.191.017-.239.918-8.107zm-10.645 6.87-3.16 1.808v5.673h6.61v-2.552l.261-.06z" transform="translate(122.04 -528.643)"/>
        <path style="display:inline;stroke-linecap:round;paint-order:markers fill stroke" d="M251.705 677.55v31.68h7.277v-2.623l15.307-3.57v-19.295l-15.307-3.57v-2.621zm.668.667h5.943v30.347h-5.943zm6.61 2.638 14.64 3.415v18.24l-14.64 3.414z" transform="translate(122.04 -528.643)"/>
    </g>
</svg>
"""


svg_vout_0 = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g transform="translate(274.205 602.638)" style="display:inline">
        <rect style="fill:#000;fill-opacity:1;stroke:none;stroke-width:3.87274;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="125.46" height="39.906" x="842.902" y="858.453" ry="6.129" transform="translate(-245.415 -680.997)"/>
        <g transform="matrix(1.11126 0 0 1.11126 -79.683 -32.848)">
            <rect style="fill:#e16100;fill-opacity:1;stroke:#0d0d0d;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="54.461" height="12.45" x="649.762" y="191.183" ry="5.433"/>
            <circle style="fill:#be5200;fill-opacity:1;stroke:#0d0d0d;stroke-width:.5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" cx="676.992" cy="197.408" r="4.438"/>
        </g>
    </g>
</svg>
"""
svg_vout_1 = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g transform="translate(274.205 602.638)" style="display:inline">
        <rect style="fill:#000;fill-opacity:1;stroke:none;stroke-width:3.87274;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="125.46" height="39.906" x="842.902" y="858.453" ry="6.129" transform="translate(-245.415 -680.997)"/>
        <g transform="matrix(1.11126 0 0 1.11126 -79.683 -32.848)">
            <rect style="fill:#e16100;fill-opacity:1;stroke:#0d0d0d;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="54.461" height="12.45" x="460.358" y="503.232" ry="5.433" transform="rotate(-30)"/>
            <circle style="fill:#be5200;fill-opacity:1;stroke:#0d0d0d;stroke-width:.5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" cx="676.992" cy="197.408" r="4.438"/>
        </g>
    </g>
</svg>
"""
svg_vout_2 = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g transform="translate(274.205 602.638)" style="display:inline">
        <rect style="fill:#000;fill-opacity:1;stroke:none;stroke-width:3.87274;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="125.46" height="39.906" x="842.902" y="858.453" ry="6.129" transform="translate(-245.415 -680.997)"/>
        <g transform="matrix(1.11126 0 0 1.11126 -79.683 -32.848)">
            <rect style="fill:#e16100;fill-opacity:1;stroke:#0d0d0d;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="54.461" height="12.45" x="140.305" y="678.772" ry="5.433" transform="rotate(-60)"/>
            <circle style="fill:#be5200;fill-opacity:1;stroke:#0d0d0d;stroke-width:.5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" cx="676.992" cy="197.408" r="4.438"/>
        </g>
    </g>
</svg>
"""
svg_vout_3 = """
<svg width="1000" height="820" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <g transform="translate(274.205 602.638)" style="display:inline">
        <rect style="fill:#000;fill-opacity:1;stroke:none;stroke-width:3.87274;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="125.46" height="39.906" x="842.902" y="858.453" ry="6.129" transform="translate(-245.415 -680.997)"/>
        <g transform="matrix(1.11126 0 0 1.11126 -79.683 -32.848)">
            <rect style="fill:#e16100;fill-opacity:1;stroke:#0d0d0d;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" width="54.461" height="12.45" x="-224.639" y="670.767" ry="5.433" transform="rotate(-90)"/>
            <circle style="fill:#be5200;fill-opacity:1;stroke:#0d0d0d;stroke-width:.5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" cx="676.992" cy="197.408" r="4.438"/>
        </g>
    </g>
</svg>
"""


class Projeto(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.useHardware = False
        
        self.values = ["0","0","0","0","0","0","0","0","0","0"]
        self.valvOutNivel = 0

        self.setStyleSheet("""
            QPushButton#openValvOut {
                qproperty-icon: url(:/images/light/arrow-rotate-left.svg);
                padding: 7px 5px;
            }
                           
            QPushButton#closeValvOut {
                qproperty-icon: url(:/images/light/arrow-rotate-right.svg);
                padding: 7px 5px;
            }
        """)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.imageWidth = 600
        self.imageHeight = self.imageWidth * 0.82

        self.widthAgua = int(self.imageWidth * 0.5)
        self.heightAgua = int(self.widthAgua * (720/500))
        self.xAgua = int(self.imageWidth * 0.373175)
        self.yAgua = int(self.imageHeight * (85.592/820))

        self.nivelAgua = 0
        self.nivelaguaHeight = int(self.heightAgua * self.nivelAgua)
        self.nivelAguaY = self.yAgua + self.heightAgua*(1 - self.nivelAgua/100)

        self.imageBase = QSvgWidget(parent=self)
        self.imageBase.renderer().load(svg_base.encode("utf-8"))
        self.imageBase.setFixedSize(self.imageWidth, self.imageHeight)

        self.imageAguaOpen = QSvgWidget(parent=self.imageBase)
        self.imageAguaOpen.renderer().load(svg_agua_open.encode("utf-8"))
        self.imageAguaOpen.setFixedSize(self.imageWidth, self.imageHeight)
        self.imageAguaOpen.hide()

        self.imageAgua = QSvgWidget(parent=self.imageBase)
        self.imageAgua.renderer().load(svg_agua.encode("utf-8"))
        self.imageAgua.setFixedSize(self.widthAgua, self.nivelaguaHeight)
        self.imageAgua.move(self.xAgua, self.nivelAguaY)

        self.imageTanque = QSvgWidget(parent=self.imageBase)
        self.imageTanque.renderer().load(svg_tanque.encode("utf-8"))
        self.imageTanque.setFixedSize(self.imageWidth, self.imageHeight)

        self.imageSensor1 = QSvgWidget(parent=self.imageBase)
        self.imageSensor1.renderer().load(svg_sensor_1_off.encode("utf-8"))
        self.imageSensor1.setFixedSize(self.imageWidth, self.imageHeight)

        self.imageSensor2 = QSvgWidget(parent=self.imageBase)
        self.imageSensor2.renderer().load(svg_sensor_2_off.encode("utf-8"))
        self.imageSensor2.setFixedSize(self.imageWidth, self.imageHeight)

        self.imageSensor3 = QSvgWidget(parent=self.imageBase)
        self.imageSensor3.renderer().load(svg_sensor_3_off.encode("utf-8"))
        self.imageSensor3.setFixedSize(self.imageWidth, self.imageHeight)

        self.imagesValvOut = [svg_vout_0, svg_vout_1, svg_vout_2, svg_vout_3]

        self.imageVOut = QSvgWidget(parent=self.imageBase)
        self.imageVOut.renderer().load(svg_vout_0.encode("utf-8"))
        self.imageVOut.setFixedSize(self.imageWidth, self.imageHeight)


        self.Sensor1 = QtWidgets.QPushButton("A: Funcional", self.imageBase)
        self.Sensor1.setCursor(QtCore.Qt.PointingHandCursor)
        self.Sensor1.move(133, 335)
        self.Sensor1.clicked.connect(lambda: self.toggleSensorMode(0))

        self.Sensor2 = QtWidgets.QPushButton("B: Funcional", self.imageBase)
        self.Sensor2.setCursor(QtCore.Qt.PointingHandCursor)
        self.Sensor2.move(133, 200)
        self.Sensor2.clicked.connect(lambda: self.toggleSensorMode(1))

        self.Sensor3 = QtWidgets.QPushButton("C: Funcional", self.imageBase)
        self.Sensor3.setCursor(QtCore.Qt.PointingHandCursor)
        self.Sensor3.move(133, 67)
        self.Sensor3.clicked.connect(lambda: self.toggleSensorMode(2))
        
        self.svgSensorsOn = [svg_sensor_1_on, svg_sensor_2_on, svg_sensor_3_on]
        self.svgSensorsOff = [svg_sensor_1_off, svg_sensor_2_off, svg_sensor_3_off]
        self.svgSensorsQOn = [svg_sensor_1_q_on, svg_sensor_2_q_on, svg_sensor_3_q_on]
        self.svgSensorsQOff = [svg_sensor_1_q_off, svg_sensor_2_q_off, svg_sensor_3_q_off]

        self.sensors = [self.imageSensor1, self.imageSensor2, self.imageSensor3]
        self.sensorButtons = [self.Sensor1, self.Sensor2, self.Sensor3]
        self.sensorMode = [0, 0, 0]

        self.btnOpenValvOut = QtWidgets.QPushButton(self.imageBase)
        self.btnOpenValvOut.setObjectName("openValvOut")
        self.btnOpenValvOut.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnOpenValvOut.move(535, 420)
        self.btnOpenValvOut.clicked.connect(self.openValvOut)

        self.btnCloseValvOut = QtWidgets.QPushButton(self.imageBase)
        self.btnCloseValvOut.setObjectName("closeValvOut")
        self.btnCloseValvOut.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnCloseValvOut.move(567, 420)
        self.btnCloseValvOut.clicked.connect(self.closeValvOut)

        self.selectSimulationMode = QtWidgets.QComboBox(self.imageBase)
        self.selectSimulationMode.setObjectName("selectSimulationMode")
        self.selectSimulationMode.setCursor(QtCore.Qt.PointingHandCursor)
        self.selectSimulationMode.currentIndexChanged.connect(self.simulationMode)
        self.selectSimulationMode.setFixedSize(150, 30)
        self.selectSimulationMode.move(30, 448)

        self.selectSimulationMode.setPlaceholderText("Modo de simulação")
        self.selectSimulationMode.addItem("Circuito de Joãozinho")
        self.selectSimulationMode.addItem("Circuito externo")

        self.selectSimulationMode.setCurrentIndex(0)


        self.Layout.addWidget(self.imageBase)

    @Slot()
    def toggleSensorMode(self, sensor: int):
        mode = (self.sensorMode[sensor] + 1) % 3
        self.sensorMode[sensor] = mode
        
        sensorLetra = ["A", "B", "C"]
        modeTexts = ["Funcional", "On", "Off"]
        modeValues = ["1", "1", "0"]
        modeSvgs = [self.svgSensorsOn, self.svgSensorsQOn, self.svgSensorsQOff]

        self.sensorButtons[sensor].setText(f"{sensorLetra[sensor]}: {modeTexts[mode]}")
        self.values[sensor] = modeValues[mode]

        if mode == 0:
            svg = self.svgSensorsOn[sensor] if self.values[sensor] == "1" else self.svgSensorsOff[sensor]
        else:
            svg = modeSvgs[mode][sensor]

        self.sensors[sensor].renderer().load(svg.encode("utf-8"))


    @Slot()
    def getIsOpen(self, data: list):
        if self.useHardware:
            return int(data[0])
        else:
            A = int(self.values[0])
            B = int(self.values[1])
            C = int(self.values[2])
            D = int(self.values[3])

            out = ((not C) and D) or not A
            # out = ((not C) and (not B) and (not A)) or ((not C) and A and D)

            return out
    
    @Slot()
    def simulationMode(self, index: int):
        if index == 0:
            self.useHardware = False
            return
        
        self.useHardware = True

    @Slot()
    def openValvOut(self):
        nivel = self.valvOutNivel + 1
        if nivel <= 3:
            self.valvOutNivel = nivel
            self.imageVOut.renderer().load(self.imagesValvOut[nivel].encode("utf-8"))
            self.values[3] = "1"

    @Slot()
    def closeValvOut(self):
        nivel = self.valvOutNivel - 1
        if nivel >= 0:
            self.valvOutNivel = nivel
            self.imageVOut.renderer().load(self.imagesValvOut[nivel].encode("utf-8"))

        if nivel <= 0:
            self.values[3] = "0"
        else:
            self.values[3] = "1"

    @Slot()
    def resetSimulation(self):
        self.selectSimulationMode.setDisabled(False)
        # self.nivelAgua = 0
        # self.nivelaguaHeight = 0
        # self.nivelAguaY = self.yAgua + self.heightAgua

        # self.imageAgua.setFixedSize(self.widthAgua, self.nivelaguaHeight)
        # self.imageAgua.move(self.xAgua, self.nivelAguaY)
        return

    @Slot(list)
    def updateSimulation(self, data: list):
        self.selectSimulationMode.setDisabled(True)

        isInOpen = int(data[0]) if self.useHardware else self.getIsOpen(data)
        nivelAgua = self.nivelAgua + (isInOpen - (self.valvOutNivel*2/3))*0.5

        if 0 <= nivelAgua <= 106:
            self.nivelAgua = nivelAgua
            self.nivelaguaHeight = int(self.heightAgua * self.nivelAgua / 100)
            self.nivelAguaY = self.yAgua + self.heightAgua * (1 - self.nivelAgua / 100)

            self.imageAgua.setFixedSize(self.widthAgua, self.nivelaguaHeight)
            self.imageAgua.move(self.xAgua, self.nivelAguaY)
        elif nivelAgua > 106:
            print("Transbordou")

        sensor_thresholds = [25, 56, 87]
        sensor_images_on = [svg_sensor_1_on, svg_sensor_2_on, svg_sensor_3_on]
        sensor_images_off = [svg_sensor_1_off, svg_sensor_2_off, svg_sensor_3_off]
        sensors = [self.imageSensor1, self.imageSensor2, self.imageSensor3]

        for i, threshold in enumerate(sensor_thresholds):
            if self.nivelAgua > threshold:
                if self.sensorMode[i] == 0:
                    sensors[i].renderer().load(sensor_images_on[i].encode("utf-8"))
                    self.values[i] = "1"
            else:
                if self.sensorMode[i] == 0:
                    sensors[i].renderer().load(sensor_images_off[i].encode("utf-8"))
                    self.values[i] = "0"

    @Slot()
    def getValues(self):
        # self.values[0] = str(1)
        return self.values