from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Qt
from PySide6.QtSvgWidgets import QSvgWidget


svg_Page2 = """
<svg width="1000" height="1000" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <rect style="display:inline;fill:#fff;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" width="1000" height="1000" ry="0"/>
    <path style="display:inline;fill:#edcf99;fill-opacity:1;stroke-width:1.16646;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M375.225 335.18h249.549v329.64H375.225z"/>
    <path style="display:inline;fill:#f4f5ed;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M0 0h1000L624.775 335.18h-249.55Z"/>
    <path style="display:inline;fill:#f3deb9;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M1000 1000V0L624.775 335.18v329.64z"/>
    <path style="display:inline;fill:#c2a676;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m0 1000 375.225-335.18V335.18L0 0Z"/>
    <path style="display:inline;fill:#d27857;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m0 1000 375.225-335.18h249.55L1000 1000Z"/>
    <path style="display:inline;fill:#a9edf3;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m194.764 686.507 119.204-106.411.458-244.045L194.764 229.16Z"/>
    <path style="display:inline;fill:#edcf99;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m314.426 336.051-.458 244.045-8.897 7.942V327.695z"/>
    <path style="display:inline;fill:#f3deb9;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M194.764 229.16 314.426 336.05l-9.355 2.636-110.307-86.539zM194.764 686.507l119.204-106.411-8.897-4.35-110.307 93.3z"/>
    <path style="display:inline;fill:#fff;fill-opacity:1;stroke-width:.689446;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M643.386 520.073v24.877l10.258 9.172v-43.221z"/>
    <path style="display:inline;fill:#e3e3e3;fill-opacity:1;stroke-width:2.12474;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M113.078 540.07V444.72l-70.34-62.892v221.135z"/>
    <path style="display:inline;fill:#fff;fill-opacity:1;stroke-width:1.5603;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M919.014 504.361v56.301l23.216 20.757v-97.815z"/>
    <path style="display:inline;fill:#a83837;fill-opacity:1;stroke-width:1.16646;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M428.621 379.847H571.38V664.82H428.621z"/>
    <g style="display:inline">
        <path style="fill:#cbcbcb;fill-opacity:1;stroke-width:.69453;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M408.928 199.772S434.16 263.827 500 263.827s91.072-64.055 91.072-64.055z"/>
        <path style="fill:#cbcbcb;fill-opacity:1;stroke-width:1.74962;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M496.915 122.13h6.17v77.642h-6.17z"/>
        <path style="fill:#9a9a9a;fill-opacity:1;stroke-width:.824063;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M447.235 199.772S443.29 185.634 500 185.634s52.765 14.138 52.765 14.138z"/>
        <path style="fill:#9a9a9a;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M476.126 115.455h47.748v6.674h-47.748z"/>
    </g>
</svg>
"""
svg_Page2_ON = """
<svg width="1000" height="1000" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <g style="display:inline">
        <path style="fill:#ffc113;fill-opacity:1;stroke-width:.69453;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M408.928 199.772S434.16 263.827 500 263.827s91.072-64.055 91.072-64.055z"/>
        <path style="fill:#ffa604;fill-opacity:1;stroke-width:1.74962;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M496.915 122.13h6.17v77.642h-6.17z"/>
        <path style="fill:#d68a00;fill-opacity:1;stroke-width:.824063;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M447.235 199.772S443.29 185.634 500 185.634s52.765 14.138 52.765 14.138z"/>
        <path style="fill:#d68a00;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M476.126 115.455h47.748v6.674h-47.748z"/>
    </g>
</svg>
"""

svg_Page3 = """
<svg width="1000" height="1000" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="e">
            <stop style="stop-color:#570b0b;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#380000;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="d">
            <stop style="stop-color:#43a0ff;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#2391ff;stop-opacity:1" offset=".347"/>
            <stop style="stop-color:#0080ff;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="c">
            <stop style="stop-color:#ac5229;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#4f2413;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="b">
            <stop style="stop-color:#f97a1e;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#cc4c05;stop-opacity:1" offset=".512"/>
            <stop style="stop-color:#9d3f0d;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="a">
            <stop style="stop-color:#ef762f;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#bf4105;stop-opacity:1" offset=".497"/>
            <stop style="stop-color:#a64109;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="i" x1="0" y1="129.242" x2="1000" y2="129.242" gradientUnits="userSpaceOnUse" gradientTransform="matrix(.90234 0 0 1 48.832 0)"/>
        <linearGradient xlink:href="#b" id="j" x1="0" y1="65.347" x2="1000" y2="65.347" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#b" id="k" x1="157.29" y1="732.615" x2="842.71" y2="732.615" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#c" id="l" x1="0" y1="971.495" x2="1000" y2="971.495" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#d" id="f" x1="0" y1="0" x2="1000" y2="1000" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#e" id="g" x1="0" y1="763.836" x2="1000" y2="763.836" gradientUnits="userSpaceOnUse"/>
        <filter style="color-interpolation-filters:sRGB" id="h" x="-.097" y="-.107" width="1.215" height="1.237">
            <feFlood result="flood" flood-opacity=".286" flood-color="#000"/>
            <feGaussianBlur result="blur" in="SourceGraphic" stdDeviation="20"/>
            <feOffset result="offset" in="blur" dx="10" dy="10"/>
            <feComposite result="comp1" operator="in" in="flood" in2="offset"/>
            <feComposite result="comp2" in="SourceGraphic" in2="comp1"/>
        </filter>
    </defs>
    <rect style="fill:url(#f);fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="1000" height="1000" ry="0"/>
    <rect style="fill:url(#g);fill-opacity:1;stroke-width:.485967;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:2.42983,4.3737;paint-order:markers stroke fill" width="1000" height="236.164" y="763.836" ry="0"/>
    <g transform="matrix(.9294 0 0 .9294 264.176 94.524)" style="filter:url(#h)">
        <path style="display:inline;fill:#3eac92" d="M312.127 292.149c10.88-28.608 18.982-61.79 18.982-97.175C331.11 87.293 256.073 0 256.073 0s-75.037 87.293-75.037 194.974c0 35.55 8.179 68.878 19.136 97.576v116.399l55.39 26.313 60.026-30.32z"/>
        <path style="display:inline;fill:#7cd8a4" d="M415.258 141.67s-52.248 13.736-80.934 55.34-22.949 95.322-22.949 95.322.634-.188.85-.248c-48.957 64.544-55.938 143.897-56.223 147.393-.284-3.48-7.237-82.49-55.898-146.961l1.521.445s5.737-53.718-22.95-95.322c-28.685-41.604-80.933-55.34-80.933-55.34s-4.456 41.874 14.242 80.315C59.093 197.666 9.807 193.926 9.807 193.926s7.742 102.516 75.746 170.522c67.733 67.735 169.565 75.666 170.377 75.728l-.002.018.082-.008.064.006-.002-.014c.812-.062 102.642-7.997 170.375-75.73 68.005-68.004 75.746-170.522 75.746-170.522s-48.727 3.687-101.277 28.256c18.81-38.495 14.342-80.512 14.342-80.512z"/>
        <path style="display:inline;opacity:.21;fill:#266659" d="M400.939 222.166c18.799-38.489 14.319-80.495 14.319-80.495s-37.863 9.96-66.823 38.59c-12.648 89.188-48.237 204.494-145.938 249.387 17.214 4.909 31.833 7.618 41.428 9.055l5.901 5.901c.232.32.483.63.772.918a7.513 7.513 0 0 0 5.329 2.207l.073-.003.073.003a7.515 7.515 0 0 0 5.329-2.207c.288-.288.54-.599.772-.918l5.901-5.901c29.127-4.363 104.552-20.434 158.373-74.255 68.004-68.004 75.745-170.522 75.745-170.522s-48.713 3.681-101.254 28.24z"/>
        <path style="display:inline;fill:#266659" d="M256.072 27.371c-4.162 0-7.535 3.395-7.535 7.583v107.603l-20.644-20.644a7.537 7.537 0 0 0-10.658 10.658l31.302 31.302v39.586l-20.644-20.646a7.537 7.537 0 0 0-10.658 10.658l31.302 31.303v39.576l-20.644-20.646a7.539 7.539 0 0 0-10.659 0 7.54 7.54 0 0 0 0 10.66l31.303 31.302v136.33l-52.76-52.76v-39.198a7.533 7.533 0 0 0-7.535-7.536 7.535 7.535 0 0 0-7.537 7.535v24.127l-23.38-23.38v-39.202a7.536 7.536 0 0 0-7.538-7.535 7.534 7.534 0 0 0-7.535 7.535v24.131l-23.389-23.388v-39.202a7.537 7.537 0 1 0-15.072 0v24.13l-56.738-56.739a7.513 7.513 0 0 0-5.328-2.207 7.537 7.537 0 0 0-5.33 12.865l56.738 56.739H69.002a7.537 7.537 0 1 0 0 15.072h39.203l23.387 23.387h-24.13a7.537 7.537 0 0 0-7.536 7.537 7.537 7.537 0 0 0 7.537 7.537h39.203l23.383 23.383h-24.131a7.537 7.537 0 1 0 0 15.072h39.203l64.824 64.824c.207.273.404.55.653.799a7.513 7.513 0 0 0 5.328 2.207c.025 0 .05-.008.074-.008.024 0 .048.008.072.008 1.93 0 3.86-.736 5.33-2.207.25-.249.446-.526.653-.799l64.824-64.824h39.201a7.536 7.536 0 1 0 0-15.072h-24.129l23.383-23.383h39.201a7.538 7.538 0 0 0 0-15.074h-24.127l23.387-23.387h39.201a7.536 7.536 0 1 0 0-15.072h-24.129l52.254-52.254a7.54 7.54 0 0 0 0-10.66 7.51 7.51 0 0 0-5.328-2.206 7.51 7.51 0 0 0-5.328 2.205l-52.258 52.258v-24.13a7.536 7.536 0 1 0-15.07 0v39.2l-23.39 23.391v-24.133a7.537 7.537 0 1 0-15.072 0v39.206l-23.382 23.38v-24.13a7.534 7.534 0 0 0-7.535-7.536 7.536 7.536 0 0 0-7.537 7.535v39.204l-52.612 52.609V285.666l31.301-31.302a7.536 7.536 0 1 0-10.656-10.66l-20.645 20.644v-39.574l31.301-31.303a7.537 7.537 0 0 0-10.656-10.658l-20.645 20.644v-39.584l31.301-31.302a7.537 7.537 0 0 0-10.656-10.658l-20.645 20.642V34.954c0-4.19-3.375-7.583-7.537-7.583zm141.424 132.497a7.53 7.53 0 0 0-6.281 3.26l-30.875 44.958-.738-4.013c-.752-4.094-4.682-6.795-8.776-6.05a7.533 7.533 0 0 0-6.049 8.774l3.473 18.893-25.842 37.627a7.537 7.537 0 0 0 12.41 8.558l25.916-37.738 18.711-3.437a7.533 7.533 0 0 0 6.05-8.774c-.753-4.094-4.678-6.797-8.774-6.05l-3.942.724 30.844-44.914a7.536 7.536 0 0 0-1.926-10.484 7.504 7.504 0 0 0-4.2-1.334zm-278.41 6.043a7.539 7.539 0 0 0-6.127 11.816l26.338 39.334-3.02-.555a7.537 7.537 0 0 0-2.723 14.826L151 234.538l26.338 39.333a7.527 7.527 0 0 0 6.21 3.258 7.539 7.539 0 0 0 6.197-11.816l-25.233-37.686 3.71-20.199a7.535 7.535 0 0 0-6.05-8.773c-4.086-.75-8.02 1.955-8.774 6.049l-.912 4.964-27.119-40.5a7.526 7.526 0 0 0-6.281-3.257z"/>
    </g>
    <g transform="matrix(.9294 0 0 .9294 37.404 -5.907)">
        <rect style="fill:#c3c3c3;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="55.908" height="185.136" x="665.326" y="358.862" ry="9.439"/>
        <path style="font-weight:600;font-size:31.3915px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Semi-Bold';letter-spacing:0;word-spacing:.840845px;fill:#303030;stroke-width:.840845;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:4.20422,7.5676;paint-order:markers stroke fill" d="M-498.627 704.173V682.2h4.08v21.974zm-15.445 0V682.2h4.081v21.974zm3.736-9.417v-3.485h12.023v3.485zm31.14 9.731q-4.52 0-7.094-2.542-2.543-2.543-2.543-7.346v-12.4h4.081v12.243q0 3.39 1.444 4.928 1.475 1.539 4.144 1.539 2.668 0 4.112-1.539 1.444-1.538 1.444-4.928v-12.243h4.018v12.4q0 4.803-2.574 7.346-2.543 2.542-7.032 2.542zm15.32-.314V682.2h3.358l9.606 16.041h-1.758l9.449-16.04h3.359l.031 21.973h-3.86l-.032-15.915h.816l-8.036 13.404h-1.821l-8.162-13.404h.942v15.915zm29.978 0V682.2h4.081v21.974zm10.014 0V682.2h9.606q3.579 0 6.278 1.382 2.7 1.38 4.207 3.83 1.507 2.448 1.507 5.775 0 3.296-1.507 5.776-1.507 2.449-4.207 3.83-2.7 1.381-6.278 1.381zm4.081-3.453h5.337q2.448 0 4.269-.941 1.82-.942 2.794-2.637 1.004-1.696 1.004-3.956 0-2.291-1.004-3.955-.973-1.695-2.794-2.637-1.82-.942-4.27-.942h-5.336zm22.1 3.673q-1.068 0-1.821-.722-.753-.753-.753-1.883 0-1.193.753-1.884.753-.722 1.82-.722 1.068 0 1.821.722.754.69.754 1.884 0 1.13-.754 1.883-.753.722-1.82.722z" transform="rotate(-90)" aria-label="HUMID."/>
    </g>
    <g transform="translate(244.838 480.474) scale(.50527)">
        <path style="fill:url(#i);fill-opacity:1;stroke-width:.949915;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:4.74957,8.54922;paint-order:markers stroke fill;filter:url(#filter75)" d="m48.832 129.242 141.44 542.778h619.456l141.44-542.778Z"/>
        <rect style="fill:url(#j);fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill;filter:url(#filter71)" width="1000" height="130.694" ry="27.724"/>
        <rect style="fill:url(#k);fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill;filter:url(#filter73)" width="685.419" height="123.434" x="157.29" y="670.898" ry="27.724"/>
    </g>
    <rect style="fill:url(#l);fill-opacity:1;stroke-width:.168834;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:.844169,1.51951;paint-order:markers stroke fill" width="1000" height="28.505" y="971.495" ry="0"/>
    <g transform="translate(0 -57.36)">
        <rect style="fill:#c3c3c3;fill-opacity:1;stroke-width:1.20175;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:6.00876,10.8158;paint-order:markers stroke fill" width="67.188" height="224.751" x="169.427" y="-287.892" ry="11.343" transform="rotate(90)"/>
        <rect style="fill:#c3c3c3;fill-opacity:1;stroke-width:1.20175;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:6.00876,10.8158;paint-order:markers stroke fill" width="67.188" height="223.724" x="260.302" y="-287.892" ry="11.343" transform="rotate(90)"/>
        <path style="font-weight:600;font-size:29.1751px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Semi-Bold';text-align:center;letter-spacing:0;word-spacing:.781477px;text-anchor:middle;fill:#303030;stroke-width:1.01049;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5.05242,9.09437;paint-order:markers stroke fill" d="M112.391 216.602q-3.018 0-5.62-.98-2.566-1.02-4.49-2.83-1.886-1.849-2.943-4.338-1.056-2.49-1.056-5.433 0-2.942 1.056-5.432 1.057-2.49 2.98-4.3 1.925-1.85 4.49-2.83 2.565-1.019 5.62-1.019 3.245 0 5.924 1.132 2.678 1.094 4.527 3.282l-3.17 2.98q-1.433-1.546-3.206-2.3-1.773-.793-3.848-.793t-3.81.679q-1.698.679-2.98 1.924-1.245 1.245-1.962 2.942-.679 1.698-.679 3.735t.679 3.735q.717 1.698 1.962 2.942 1.282 1.245 2.98 1.924 1.735.68 3.81.68t3.848-.755q1.773-.792 3.207-2.377l3.169 3.018q-1.849 2.15-4.527 3.282-2.679 1.132-5.96 1.132zm33.424-.377v-26.407h4.904v26.407zm-18.56 0v-26.407h4.904v26.407zm4.489-11.318v-4.187h14.448v4.187zm37.423 11.695q-5.433 0-8.526-3.056-3.056-3.055-3.056-8.827v-14.901h4.905v14.712q0 4.074 1.735 5.923 1.773 1.848 4.98 1.848 3.206 0 4.942-1.848 1.735-1.849 1.735-5.923v-14.713h4.829v14.902q0 5.772-3.094 8.827-3.056 3.056-8.45 3.056zm26.219-.377-11.544-26.407h5.319l10.299 23.88h-3.056l10.412-23.88h4.904l-11.506 26.407zm14.561 0 11.884-26.407h4.828l11.921 26.407h-5.13l-10.224-23.804h1.962l-10.186 23.804zm5.47-6.112 1.32-3.848h14.26l1.321 3.848z" aria-label="CHUVA"/>
        <path d="M108.781 307.364q-3.094 0-5.931-.81-2.837-.848-4.568-2.174l2.026-4.495q1.658 1.18 3.905 1.953 2.284.736 4.605.736 1.768 0 2.837-.331 1.105-.368 1.62-.995.516-.626.516-1.436 0-1.032-.81-1.621-.81-.627-2.137-.995-1.326-.405-2.947-.737-1.584-.368-3.205-.884-1.584-.516-2.91-1.326t-2.174-2.137q-.81-1.326-.81-3.389 0-2.21 1.179-4.015 1.215-1.842 3.61-2.91 2.431-1.106 6.078-1.106 2.432 0 4.79.59 2.357.552 4.162 1.694l-1.842 4.531q-1.805-1.031-3.61-1.51-1.805-.516-3.537-.516-1.731 0-2.836.405-1.105.406-1.584 1.069-.48.626-.48 1.473 0 .995.811 1.621.81.59 2.137.958 1.326.368 2.91.737 1.621.368 3.205.847 1.621.48 2.947 1.29 1.327.81 2.137 2.136.847 1.326.847 3.352 0 2.174-1.215 3.98-1.216 1.804-3.647 2.91-2.395 1.105-6.079 1.105zm29.09 0q-3.057 0-5.673-.995-2.578-.995-4.494-2.8-1.879-1.805-2.947-4.236-1.032-2.432-1.032-5.305 0-2.874 1.032-5.305 1.068-2.431 2.984-4.236 1.916-1.806 4.494-2.8 2.579-.995 5.6-.995 3.057 0 5.6.995 2.578.994 4.457 2.8 1.915 1.805 2.984 4.236 1.068 2.395 1.068 5.305 0 2.873-1.068 5.341-1.069 2.432-2.984 4.237-1.879 1.768-4.458 2.763-2.542.995-5.562.995zm-.036-5.084q1.731 0 3.168-.59 1.473-.59 2.579-1.694 1.105-1.105 1.694-2.616.627-1.51.627-3.352 0-1.842-.627-3.352-.59-1.51-1.694-2.616-1.069-1.105-2.542-1.695-1.474-.59-3.205-.59-1.732 0-3.205.59-1.437.59-2.542 1.695-1.105 1.105-1.732 2.616-.589 1.51-.589 3.352 0 1.805.59 3.352.626 1.51 1.694 2.616 1.105 1.105 2.579 1.694 1.473.59 3.205.59zm20.138 4.641v-25.787h5.968v20.925h12.93v4.862z" style="font-weight:700;font-size:36.8389px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Bold';letter-spacing:1.53496px;word-spacing:.383739px;fill:#303030;stroke-width:.383739;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1.91869,3.45365;paint-order:markers stroke fill" aria-label="SOL"/>
    </g>
    <rect style="fill:#303030;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="23.617" height="737.123" x="58.529" y="112.067" ry="6.418"/>
    <rect style="fill:#303030;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="229.362" height="26.139" x="58.529" y="439.853" ry="6.418"/>
</svg>
"""
svg_Page3_ON = """
<svg width="1000" height="1000" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="e">
            <stop style="stop-color:#570b0b;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#380000;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="d">
            <stop style="stop-color:#43a0ff;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#2391ff;stop-opacity:1" offset=".347"/>
            <stop style="stop-color:#0080ff;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="c">
            <stop style="stop-color:#ac5229;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#4f2413;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="b">
            <stop style="stop-color:#f97a1e;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#cc4c05;stop-opacity:1" offset=".512"/>
            <stop style="stop-color:#9d3f0d;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="a">
            <stop style="stop-color:#ef762f;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#bf4105;stop-opacity:1" offset=".497"/>
            <stop style="stop-color:#a64109;stop-opacity:1" offset="1"/>
        </linearGradient>
    </defs>
    <path style="fill:#b3d6f8;fill-opacity:1;stroke-width:8;stroke-linecap:round;stroke-linejoin:round;paint-order:stroke fill markers" d="M283.979 497.032c-3.551-.06-5.891.182-5.891.182h3.387a6.402 6.402 0 0 1 6.416 6.418v13.303a6.402 6.402 0 0 1-6.416 6.418h-.868s7.673 1.95 10.051 4.69c2.378 2.741 3.857 3.917 5.135 7.548.149.422.282 1.302.404 1.873h44.27c-2.383-6.268-5.42-13.718-8.303-17.694-5.955-8.214-12.951-14.474-20.734-17.916-7.784-3.441-17.895-4.212-23.54-4.64a66.894 66.894 0 0 0-3.911-.182z" transform="translate(0 -57.36)"/>
</svg>
"""

svg_Page4 = """
<svg width="1000" height="1000" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <path style="display:inline;fill:#e4e6e5;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M331.667 173.535h508.924v661.28H331.667z" transform="matrix(1.51222 0 0 1.51222 -386.355 -262.422)"/>
    <path style="display:inline;fill:#828280;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M372.034 216.662h428.189v575.026H372.034z" transform="matrix(1.51222 0 0 1.51222 -386.355 -262.422)"/>
    <g style="display:inline">
        <path style="display:inline;fill:#d5d9da;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M372.74 351.69h396.357v58.529H372.74z" transform="matrix(1.51222 0 0 1.51222 -387.422 -76.087)"/>
        <path style="display:inline;fill:#aaaba6;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M372.74 362.454h396.357v3.384H372.74zM372.74 395.128h396.357v3.384H372.74z" transform="matrix(1.51222 0 0 1.51222 -387.422 -75.373)"/>
    </g>
    <g style="display:inline">
        <g transform="matrix(1.51222 0 0 1.51222 -386.355 -260.481)">
            <rect style="display:inline;fill:#848580;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="8.728" height="8.215" x="802.405" y="506.191" ry="0"/>
            <rect style="display:inline;fill:#5c5c5a;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="7.393" height="29.759" x="797.466" y="495.015" ry="3.267"/>
            <rect style="fill:#aaaba6;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="10.256" height="32.855" x="790.973" y="493.462" ry="1.906"/>
            <path style="display:inline;fill:#2e2e27;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M813.3 496.457a4.8 4.8 0 0 0-4.81 4.81v18.061a4.8 4.8 0 0 0 4.81 4.81h12.526a4.799 4.799 0 0 0 4.809-4.81v-18.06a4.799 4.799 0 0 0-4.809-4.811zm12.848 11.088a2.754 2.754 0 0 1 2.752 2.754 2.754 2.754 0 0 1-2.752 2.752 2.754 2.754 0 0 1-2.753-2.752 2.754 2.754 0 0 1 2.753-2.754z"/>
        </g>
        <path style="display:inline;fill:#e4e6e5;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M773.205 220.256h22.077v565.271h-22.077z" transform="matrix(1.51222 0 0 1.51222 -386.355 -260.481)"/>
    </g>
    <path style="display:inline;fill:#e4e6e5;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M389.905 536.573h153.336V721.36H389.905z" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
    <path style="display:inline;fill:#f9fbfa;fill-opacity:1;stroke-width:.813489;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:4.06745,7.3214;paint-order:markers stroke fill" d="M389.905 567.824h153.336V690.11H389.905z" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
    <path style="display:inline;fill:#fa1515;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" d="M392.399 569.824h45.198v11.799h-45.198z" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
    <path style="display:inline;fill:#3e3e3c;fill-opacity:1;stroke:none;stroke-width:.44776;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers stroke fill" d="M414.998 544.35a7.701 7.701 0 0 0-7.7 7.7 7.701 7.701 0 0 0 7.7 7.702 7.701 7.701 0 0 0 7.701-7.701 7.701 7.701 0 0 0-7.7-7.701zm-2.854 4.078a.44.44 0 0 1 .311.13l2.585 2.585 2.585-2.585a.438.438 0 0 1 .621-.002.442.442 0 0 1 0 .624l-2.583 2.585 2.583 2.586a.438.438 0 0 1 .002.62.442.442 0 0 1-.624 0l-2.584-2.585-2.585 2.585a.44.44 0 1 1-.622-.62l2.585-2.586-2.585-2.585a.44.44 0 0 1 0-.622v-.002a.435.435 0 0 1 .311-.128z" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
    <path d="M410.295 579.558v-7.67h1.775v6.224h3.846v1.446zm7.631 0v-7.012l.767.767h-2.3v-1.424h3.308v7.669z" style="font-weight:700;font-size:10.9556px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Bold';letter-spacing:.684721px;word-spacing:.342361px;display:inline;fill:#fff;stroke-width:.171181;stroke-linecap:round;paint-order:markers stroke fill" aria-label="L1" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
    <path style="fill:#15fa23;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" transform="translate(-779.505 -1402.487) scale(3.02478)" d="M392.399 569.824h45.198v11.799h-45.198z"/>
    <path style="fill:#3e3e3c;fill-opacity:1;stroke:none;stroke-width:.44776;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers stroke fill" d="M414.998 544.35a7.701 7.701 0 0 0-7.7 7.7 7.701 7.701 0 0 0 7.7 7.702 7.701 7.701 0 0 0 7.701-7.701 7.701 7.701 0 0 0-7.7-7.701zm-2.854 4.078a.44.44 0 0 1 .311.13l2.585 2.585 2.585-2.585a.438.438 0 0 1 .621-.002.442.442 0 0 1 0 .624l-2.583 2.585 2.583 2.586a.438.438 0 0 1 .002.62.442.442 0 0 1-.624 0l-2.584-2.585-2.585 2.585a.44.44 0 1 1-.622-.62l2.585-2.586-2.585-2.585a.44.44 0 0 1 0-.622v-.002a.435.435 0 0 1 .311-.128zM414.998 699.157a7.701 7.701 0 0 0-7.7 7.701 7.701 7.701 0 0 0 7.7 7.701 7.701 7.701 0 0 0 7.701-7.7 7.701 7.701 0 0 0-7.7-7.702zm-2.854 4.079a.44.44 0 0 1 .311.13l2.585 2.584 2.585-2.585a.438.438 0 0 1 .621-.002.442.442 0 0 1 0 .625l-2.583 2.585 2.583 2.585a.438.438 0 0 1 .002.62.442.442 0 0 1-.624 0l-2.584-2.584-2.585 2.585a.44.44 0 1 1-.622-.621l2.585-2.585-2.585-2.585a.44.44 0 0 1 0-.623v-.002a.435.435 0 0 1 .311-.128z" transform="translate(-779.505 -1402.487) scale(3.02478)"/>
    <path d="M460.246 579.624v-7.67h1.775v6.223h3.845v1.447zm6.754 0v-1.15l2.958-2.794q.35-.318.515-.57.164-.252.22-.46.065-.208.065-.384 0-.46-.318-.7-.307-.253-.91-.253-.481 0-.897.186-.406.187-.69.581l-1.293-.833q.438-.657 1.227-1.04.788-.384 1.818-.384.855 0 1.49.285.647.274.997.778.362.504.362 1.205 0 .373-.099.745-.087.362-.372.767-.274.405-.811.91l-2.454 2.31-.34-.646h4.328v1.447z" style="font-weight:700;font-size:10.9556px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Bold';letter-spacing:.684721px;word-spacing:.342361px;fill:#fff;stroke-width:.171181;stroke-linecap:round;paint-order:markers stroke fill" aria-label="L2" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
    <path style="display:inline;fill:#c6c6c4;fill-opacity:1;stroke-width:1.89902;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:9.49509,17.0911;paint-order:markers stroke fill" transform="translate(-779.505 -1402.487) scale(3.02478)" d="M392.399 676.311h45.198v11.799h-45.198z"/>
    <path style="font-weight:700;font-size:10.9556px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Bold';letter-spacing:.684721px;word-spacing:.342361px;display:inline;stroke-width:.171181;stroke-linecap:round;paint-order:markers stroke fill" d="M415.491 686.176q-.887 0-1.654-.285-.756-.295-1.315-.832-.559-.537-.876-1.26-.307-.723-.307-1.589 0-.865.307-1.588.317-.723.876-1.26.57-.537 1.326-.822.756-.296 1.654-.296.997 0 1.797.35.81.34 1.358 1.009l-1.139 1.052q-.394-.45-.876-.669-.483-.23-1.052-.23-.537 0-.986.175-.45.176-.778.504-.329.33-.515.778-.175.45-.175.997 0 .548.175.997.186.45.515.778.329.329.778.504t.986.175q.57 0 1.052-.219.482-.23.876-.69l1.14 1.052q-.548.668-1.36 1.019-.799.35-1.807.35z" aria-label="C" transform="translate(-779.505 -1402.487) scale(3.02478)"/>
    <path style="display:inline;fill:#2515fa;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" transform="translate(-623.66 -1402.487) scale(3.02478)" d="M392.399 569.824h45.198v11.799h-45.198z"/>
    <path style="display:inline;fill:#3e3e3c;fill-opacity:1;stroke:none;stroke-width:.44776;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers stroke fill" d="M414.998 544.35a7.701 7.701 0 0 0-7.7 7.7 7.701 7.701 0 0 0 7.7 7.702 7.701 7.701 0 0 0 7.701-7.701 7.701 7.701 0 0 0-7.7-7.701zm-2.854 4.078a.44.44 0 0 1 .311.13l2.585 2.585 2.585-2.585a.438.438 0 0 1 .621-.002.442.442 0 0 1 0 .624l-2.583 2.585 2.583 2.586a.438.438 0 0 1 .002.62.442.442 0 0 1-.624 0l-2.584-2.585-2.585 2.585a.44.44 0 1 1-.622-.62l2.585-2.586-2.585-2.585a.44.44 0 0 1 0-.622v-.002a.435.435 0 0 1 .311-.128zM414.998 699.157a7.701 7.701 0 0 0-7.7 7.701 7.701 7.701 0 0 0 7.7 7.701 7.701 7.701 0 0 0 7.701-7.7 7.701 7.701 0 0 0-7.7-7.702zm-2.854 4.079a.44.44 0 0 1 .311.13l2.585 2.584 2.585-2.585a.438.438 0 0 1 .621-.002.442.442 0 0 1 0 .625l-2.583 2.585 2.583 2.585a.438.438 0 0 1 .002.62.442.442 0 0 1-.624 0l-2.584-2.584-2.585 2.585a.44.44 0 1 1-.622-.621l2.585-2.585-2.585-2.585a.44.44 0 0 1 0-.623v-.002a.435.435 0 0 1 .311-.128z" transform="translate(-623.66 -1402.487) scale(3.02478)"/>
    <path d="M408.734 579.492v-7.669h1.775v6.223h3.846v1.446zm9.35.132q-.799 0-1.588-.209-.788-.219-1.336-.613l.69-1.359q.438.318 1.019.504.58.187 1.172.187.668 0 1.052-.263.383-.263.383-.723 0-.439-.34-.69-.339-.253-1.095-.253h-.81v-1.172l2.136-2.421.197.635h-4.02v-1.424h5.367v1.15l-2.125 2.422-.898-.515h.515q1.413 0 2.136.635.723.636.723 1.633 0 .646-.34 1.216-.34.558-1.04.909-.702.35-1.797.35z" style="font-weight:700;font-size:10.9556px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Bold';letter-spacing:.684721px;word-spacing:.342361px;display:inline;fill:#fff;stroke-width:.171181;stroke-linecap:round;paint-order:markers stroke fill" aria-label="L3" transform="translate(-623.66 -1402.487) scale(3.02478)"/>
    <path style="display:inline;fill:#c6c6c4;fill-opacity:1;stroke-width:1.89902;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:9.49509,17.0911;paint-order:markers stroke fill" transform="translate(-623.66 -1402.487) scale(3.02478)" d="M392.399 676.311h45.198v11.799h-45.198z"/>
    <path style="fill:#3e3e3c;stroke-width:1.62273;stroke-linecap:round;paint-order:markers stroke fill" d="m439.22 590.377-1.08 1.152h.975l1.448-1.152zm-5.453.073v5.936h1.249v-5.936zm24.348 0v5.936h1.248v-5.936zm20.04 0v2.088c-.1-.11-.21-.206-.336-.28-.272-.16-.59-.24-.952-.24-.405 0-.77.09-1.096.271a2.026 2.026 0 0 0-.776.769c-.187.33-.28.722-.28 1.176 0 .448.094.837.28 1.168.192.33.45.588.776.775.326.181.69.273 1.096.273.379 0 .701-.08.968-.24.144-.086.268-.197.376-.329v.505h1.192v-5.936zm-56.708.335v5.6h1.296v-1.56h1.128c.02 0 .037-.004.058-.004l1.078 1.565h1.4l-1.252-1.797.012-.004c.363-.16.643-.39.84-.688.198-.304.296-.663.296-1.08 0-.634-.216-1.13-.648-1.488-.432-.362-1.037-.544-1.816-.544zm25.348 0v5.6h1.296v-2.04h2.592v-1.04h-2.592v-1.48h2.936v-1.04zm44.38 0v5.6h1.296v-2.04h2.592v-1.04h-2.592v-1.48h2.936v-1.04zm-29.76.345v.951h-.664v.96h.664v1.865c0 .512.142.898.424 1.16.283.255.677.384 1.184.384.192 0 .376-.022.552-.064a1.43 1.43 0 0 0 .464-.209l-.336-.88a.8.8 0 0 1-.504.16.53.53 0 0 1-.392-.144c-.096-.101-.144-.242-.144-.423v-1.848h1.072v-.96h-1.072v-.952zm-38.672.711h1.056c.4 0 .699.086.896.257.197.17.296.41.296.72 0 .303-.099.543-.296.72-.197.17-.496.255-.896.255h-1.056zm7.212.176c-.437 0-.83.096-1.176.288a2.117 2.117 0 0 0-.824.784 2.19 2.19 0 0 0-.296 1.145c0 .426.101.807.304 1.143.203.33.488.593.856.785.374.192.806.288 1.296.288.39 0 .733-.06 1.032-.177a1.97 1.97 0 0 0 .744-.52l-.664-.72a1.458 1.458 0 0 1-1.08.416c-.256 0-.48-.045-.672-.136a1.082 1.082 0 0 1-.44-.407 1.17 1.17 0 0 1-.117-.32h3.253l.016-.168c.005-.064.008-.12.008-.168 0-.464-.098-.862-.295-1.192a1.967 1.967 0 0 0-.809-.769 2.352 2.352 0 0 0-1.136-.272zm8.936 0c-.437 0-.83.096-1.176.288a2.117 2.117 0 0 0-.824.784 2.19 2.19 0 0 0-.296 1.145c0 .426.101.807.304 1.143.203.33.488.593.856.785.374.192.806.288 1.296.288.39 0 .733-.06 1.032-.177a1.97 1.97 0 0 0 .744-.52l-.664-.72a1.458 1.458 0 0 1-1.08.416 1.56 1.56 0 0 1-.672-.136 1.082 1.082 0 0 1-.44-.407 1.17 1.17 0 0 1-.117-.32h3.253l.016-.168c.005-.064.008-.12.008-.168 0-.464-.098-.862-.296-1.192a1.966 1.966 0 0 0-.807-.769 2.355 2.355 0 0 0-1.137-.272zm15.284 0c-.341 0-.677.046-1.008.137-.33.09-.613.218-.848.383l.448.873c.155-.123.341-.22.56-.288.224-.075.45-.113.68-.113.336 0 .584.075.744.224.165.15.249.357.249.624h-.993c-.437 0-.792.057-1.064.169-.272.106-.472.255-.6.447a1.222 1.222 0 0 0-.184.672c0 .246.064.467.192.665.128.197.312.354.552.472.24.112.529.168.865.168.378 0 .687-.073.927-.217.17-.102.289-.249.384-.417v.57h1.168v-2.457c0-.656-.181-1.139-.544-1.448-.362-.31-.872-.464-1.528-.464zm12.9 0c-.341 0-.677.046-1.008.137-.33.09-.613.218-.848.383l.448.873c.155-.123.341-.22.56-.288.224-.075.45-.113.68-.113.336 0 .585.075.745.224.165.15.247.357.247.624h-.992c-.437 0-.791.057-1.063.169-.272.106-.473.255-.601.447a1.222 1.222 0 0 0-.184.672c0 .246.064.467.192.665.128.197.312.354.552.472.24.112.528.168.864.168.38 0 .688-.073.928-.217.17-.102.29-.25.385-.419v.572h1.167v-2.457c0-.656-.181-1.139-.544-1.448-.362-.31-.872-.464-1.528-.464zm16.196 0c-.437 0-.829.096-1.176.288a2.117 2.117 0 0 0-.824.784 2.19 2.19 0 0 0-.296 1.145c0 .426.102.807.304 1.143.203.33.488.593.856.785.374.192.806.288 1.296.288.39 0 .733-.06 1.032-.177a1.97 1.97 0 0 0 .744-.52l-.664-.72a1.458 1.458 0 0 1-1.08.416c-.256 0-.48-.045-.672-.136a1.082 1.082 0 0 1-.44-.407 1.17 1.17 0 0 1-.117-.32h3.253l.016-.168c.005-.064.008-.12.008-.168 0-.464-.098-.862-.295-1.192a1.967 1.967 0 0 0-.809-.769 2.352 2.352 0 0 0-1.136-.272zm15.284 0c-.341 0-.677.046-1.008.137-.33.09-.613.218-.848.383l.448.873c.155-.123.342-.22.56-.288.224-.075.45-.113.68-.113.336 0 .584.075.744.224.165.15.248.357.248.624h-.992c-.437 0-.792.057-1.064.169-.272.106-.472.255-.6.447a1.222 1.222 0 0 0-.184.672c0 .246.064.467.192.665.128.197.312.354.552.472.24.112.528.168.864.168.379 0 .689-.073.929-.217.17-.102.288-.25.383-.418v.57h1.168v-2.456c0-.656-.18-1.139-.544-1.448-.362-.31-.872-.464-1.528-.464zm5.62 0c-.416 0-.773.062-1.072.184-.298.118-.528.28-.688.489a1.174 1.174 0 0 0-.232.72c0 .245.046.445.137.6.096.154.22.277.375.368.155.09.326.16.512.207.187.043.371.078.552.104.187.027.358.054.513.08a1.1 1.1 0 0 1 .367.12c.096.049.144.123.144.225 0 .122-.06.218-.183.288-.118.069-.32.104-.609.104a2.884 2.884 0 0 1-1.496-.416l-.416.895c.198.134.464.245.8.336.342.085.697.129 1.065.129.432 0 .797-.06 1.095-.177.304-.117.536-.277.696-.48.16-.207.24-.445.24-.712 0-.245-.048-.442-.144-.592a1.012 1.012 0 0 0-.376-.36c-.15-.09-.317-.16-.504-.207a4.14 4.14 0 0 0-.56-.104 8.852 8.852 0 0 1-.504-.089 1.34 1.34 0 0 1-.375-.128.261.261 0 0 1-.137-.24c0-.117.064-.213.192-.288.128-.075.331-.112.608-.112.198 0 .4.024.608.072.213.043.424.125.632.248l.416-.888a2.433 2.433 0 0 0-.76-.28 4.338 4.338 0 0 0-.896-.096zm5.284 0c-.437 0-.829.096-1.176.288a2.117 2.117 0 0 0-.824.784 2.19 2.19 0 0 0-.296 1.145c0 .426.101.807.304 1.143.203.33.488.593.856.785.374.192.806.288 1.296.288.39 0 .733-.06 1.032-.177a1.97 1.97 0 0 0 .744-.52l-.664-.72a1.458 1.458 0 0 1-1.08.416c-.256 0-.48-.045-.672-.136a1.082 1.082 0 0 1-.44-.407 1.17 1.17 0 0 1-.117-.32h3.253l.016-.168c.005-.064.008-.12.008-.168 0-.464-.098-.862-.295-1.192a1.967 1.967 0 0 0-.809-.769 2.352 2.352 0 0 0-1.136-.272zm-79.496.944c.214 0 .4.048.56.144a.965.965 0 0 1 .488.752h-2.103a1.11 1.11 0 0 1 .111-.36.952.952 0 0 1 .376-.392c.166-.096.355-.144.568-.144zm8.936 0c.214 0 .4.048.56.144a.965.965 0 0 1 .488.752h-2.103a1.11 1.11 0 0 1 .111-.36.952.952 0 0 1 .376-.392c.166-.096.355-.144.568-.144zm44.38 0c.213 0 .4.048.56.144a.965.965 0 0 1 .489.752h-2.104a1.11 1.11 0 0 1 .11-.36.954.954 0 0 1 .377-.392c.166-.096.355-.144.568-.144zm26.189 0c.213 0 .4.048.56.144a.965.965 0 0 1 .488.752h-2.104a1.11 1.11 0 0 1 .112-.36.952.952 0 0 1 .375-.392c.166-.096.355-.144.569-.144zm-32.385.08c.203 0 .387.049.552.145.166.096.296.232.392.408.102.176.152.389.152.64 0 .245-.05.458-.152.64a1.032 1.032 0 0 1-.392.408 1.08 1.08 0 0 1-.552.144c-.208 0-.394-.048-.56-.144a1.09 1.09 0 0 1-.4-.409 1.349 1.349 0 0 1-.144-.64c0-.25.048-.463.144-.64a1.09 1.09 0 0 1 .4-.407c.166-.096.352-.144.56-.144zm-22.94 1.544H455v.44a.87.87 0 0 1-.36.44 1.094 1.094 0 0 1-.56.145c-.22 0-.393-.046-.521-.137a.463.463 0 0 1-.184-.384c0-.144.053-.264.16-.36.112-.096.315-.144.608-.144zm12.9 0h.856v.44a.87.87 0 0 1-.36.44 1.094 1.094 0 0 1-.56.145c-.218 0-.392-.046-.52-.137a.463.463 0 0 1-.183-.384c0-.144.052-.264.159-.36.112-.096.315-.144.608-.144zm31.48 0h.856v.44a.869.869 0 0 1-.36.44 1.094 1.094 0 0 1-.56.145c-.218 0-.392-.046-.52-.137a.463.463 0 0 1-.184-.384c0-.144.054-.264.16-.36.112-.096.315-.144.608-.144zm-8.509 12.117a2.9 2.9 0 0 0-1.065.19 2.54 2.54 0 0 0-.856.53c-.24.23-.428.503-.564.814-.132.31-.196.652-.196 1.024s.064.713.196 1.023c.136.31.324.581.564.812.24.23.525.408.85.535.33.123.684.184 1.065.184.433 0 .822-.074 1.166-.225.348-.15.64-.369.875-.656l-.736-.678c-.169.198-.357.345-.564.443a1.62 1.62 0 0 1-.678.143c-.23 0-.441-.039-.634-.114a1.445 1.445 0 0 1-.504-.323 1.537 1.537 0 0 1-.33-.504 1.74 1.74 0 0 1-.113-.64c0-.236.038-.451.113-.644a1.455 1.455 0 0 1 .834-.827c.193-.075.403-.111.634-.111.245 0 .471.047.678.146.207.094.395.238.564.431l.736-.679a2.224 2.224 0 0 0-.875-.65 2.864 2.864 0 0 0-1.16-.224zm-39.288 1.007c-.366 0-.689.067-.97.204-.28.136-.5.324-.656.558l.691.443a.93.93 0 0 1 .368-.31c.148-.067.307-.098.478-.098.214 0 .376.043.485.133.113.085.172.21.172.374a.865.865 0 0 1-.152.45 1.67 1.67 0 0 1-.276.304l-1.58 1.493v.611h3.095v-.77h-1.763l.945-.89c.191-.18.333-.341.43-.486a1.23 1.23 0 0 0 .2-.408c.035-.133.051-.264.051-.396 0-.25-.062-.465-.19-.644a1.198 1.198 0 0 0-.532-.415 1.93 1.93 0 0 0-.796-.152zm-15.511.07v4.092h2.999v-.77h-2.051v-3.322zm3.43 0v.76h.817v3.332h.948v-4.092zm6.861 0v4.092h3.002v-.77h-2.054v-3.322zm10.97 0v4.092h2.998v-.77h-2.051v-3.322zm3.81 0v.76h1.739l-.84.952v.628h.431c.269 0 .466.043.586.133.121.09.181.214.181.37 0 .164-.066.29-.203.384-.136.093-.326.142-.564.142-.21 0-.418-.035-.624-.1a1.904 1.904 0 0 1-.542-.27l-.37.726c.194.14.432.248.712.326.28.074.565.11.85.11.39 0 .707-.061.957-.186s.437-.286.558-.485c.12-.202.18-.417.18-.647 0-.354-.129-.645-.386-.871-.18-.159-.423-.26-.723-.308l.922-1.048v-.616zm29.39 5.43a.649.649 0 0 0-.648.65v9.169l-.516 1.302H466.25v-5.464h-5.575v-5.556h-1.407v5.556h-9.658v-5.556h-1.407v5.556h-9.657v-5.556h-1.407v5.556h-5.575v16.04h34.686v-5.222h20.148l-.527 1.327-.513 1.297-.07.177a.649.649 0 0 0 1.205.479l.26-.656c.479-1.315.088-.26.513-1.297l3.059-7.736v-9.416c0-.36-.29-.65-.65-.65zm-55.44 7.28h30.391v11.803zm-1.05 1.21 29.834 11.584h-29.833zm33.064 3.928h21.752l-1.094 2.76H466.25zm23.414 5.38c-.36 0-.65.291-.65.65v9.591a.65.65 0 1 0 1.3 0v-9.59c0-.36-.291-.65-.65-.65zm.018 12.622c-.446 0-.819.067-1.116.203-.293.13-.513.308-.662.534-.144.22-.216.466-.216.736 0 .253.05.46.148.622.104.162.237.293.4.392.161.1.34.18.533.244.199.063.394.117.588.162.198.04.379.085.541.135.162.045.293.106.392.182.099.072.148.171.148.297 0 .1-.031.188-.094.264a.633.633 0 0 1-.297.183c-.131.04-.305.06-.52.06a2.738 2.738 0 0 1-1.562-.493l-.372.824c.212.163.491.296.838.4.347.099.71.148 1.088.148.45 0 .822-.068 1.115-.203.297-.135.521-.313.67-.534.148-.22.222-.464.222-.73a1.124 1.124 0 0 0-.547-1.007 2.259 2.259 0 0 0-.54-.236 8.673 8.673 0 0 0-.589-.156c-.194-.045-.372-.09-.534-.135a1.22 1.22 0 0 1-.392-.176.358.358 0 0 1-.148-.297c0-.103.029-.194.088-.27a.6.6 0 0 1 .29-.196c.135-.05.309-.074.52-.074.212 0 .429.03.65.094.22.059.441.15.662.277l.338-.831a2.473 2.473 0 0 0-.764-.311 3.605 3.605 0 0 0-.878-.108z" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
    <path d="M517.971 686.583q-1.015 0-1.945-.266-.93-.278-1.498-.712l.665-1.474q.543.386 1.28.64.75.242 1.51.242.58 0 .93-.109.363-.12.532-.326.169-.206.169-.471 0-.338-.266-.532-.266-.205-.7-.326-.435-.133-.967-.242-.52-.12-1.05-.29-.52-.169-.955-.434-.435-.266-.713-.7-.265-.436-.265-1.112 0-.725.386-1.317.399-.604 1.184-.954.797-.363 1.993-.363.797 0 1.57.194.773.18 1.365.555l-.604 1.486q-.591-.338-1.183-.495-.592-.17-1.16-.17t-.93.134q-.363.133-.52.35-.157.205-.157.483 0 .326.266.532.266.193.7.314.436.12.955.241.532.121 1.051.278.531.157.966.423.435.266.701.7.278.435.278 1.1 0 .712-.399 1.304-.398.592-1.196.955-.785.362-1.993.362z" style="font-weight:700;font-size:14.3398px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Bold';text-align:center;letter-spacing:-.177007px;word-spacing:.0746862px;text-anchor:middle;fill:#000;fill-opacity:1;stroke-width:.503315;stroke-linecap:round;stroke-linejoin:round;paint-order:stroke fill markers" aria-label="S" transform="translate(-935.35 -1402.487) scale(3.02478)"/>
</svg>
"""

svg_Page5_S = """
<svg width="1000" height="500" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="a">
            <stop style="stop-color:#723636;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#572b2b;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="b" x1="192.703" y1="487.034" x2="192.877" y2="499.26" gradientUnits="userSpaceOnUse"/>
    </defs>
    <g style="display:inline">
        <path style="display:inline;fill:#848484;fill-opacity:1;stroke:none;stroke-width:.05;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M741.402 456.969v27.222h7.778V456.97zm-389.617 1.767v27.223h7.78v-27.223z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
        <path d="M313.054 462.982q-1.963 0-4.061-.135-2.031-.068-4.197-.27-2.099-.272-3.994-.542-1.896-.339-3.452-.745v-7.92q2.03.203 4.603.338 2.572.136 5.348.203 2.775.068 5.28.068 2.572 0 4.4-.406 1.895-.474 2.91-1.557 1.016-1.15 1.016-3.114v-1.828q0-2.234-1.354-3.384-1.286-1.219-3.723-1.219h-4.265q-7.175 0-11.034-3.114-3.79-3.181-3.79-10.763v-2.437q0-7.311 4.196-10.696 4.197-3.384 11.982-3.384 2.776 0 5.483.27 2.776.271 5.28.677 2.573.339 4.4.745v7.92q-3.113-.203-6.972-.406-3.79-.203-7.04-.203-2.302 0-4.13.474-1.76.406-2.707 1.624-.948 1.219-.948 3.453v1.354q0 2.64 1.49 3.79 1.489 1.151 4.4 1.151h4.941q4.536 0 7.446 1.693 2.979 1.624 4.4 4.535 1.49 2.911 1.49 6.634v2.843q0 5.89-2.234 9.004-2.166 3.113-6.093 4.264-3.858 1.083-9.07 1.083zm42.828-.067q-4.13 0-7.718-.677-3.587-.745-6.295-2.505-2.64-1.828-4.13-5.01-1.421-3.249-1.421-8.258v-33.982h10.019v33.914q0 2.776 1.083 4.4 1.15 1.625 3.25 2.37 2.165.744 5.212.744 2.978 0 5.077-.744 2.166-.745 3.249-2.37 1.15-1.624 1.15-4.4v-33.914h10.087v33.982q0 5.01-1.49 8.259-1.488 3.181-4.129 5.01-2.64 1.76-6.227 2.504-3.52.677-7.717.677zm26.715-.339v-50.093h21.12q2.438 0 4.943.609 2.572.542 4.67 2.302 2.167 1.692 3.453 5.144 1.354 3.453 1.354 9.139t-1.354 9.206q-1.286 3.52-3.385 5.348-2.098 1.828-4.535 2.437-2.437.61-4.739.61-1.218 0-2.843-.068-1.625-.136-3.317-.339-1.625-.203-3.046-.338-1.422-.203-2.302-.339v16.382zm10.02-24.302h9.95q1.76 0 2.979-.812 1.286-.88 1.895-2.708.61-1.895.61-5.01 0-3.046-.678-4.806-.609-1.827-1.827-2.64-1.151-.812-2.776-.812h-10.154zm43.368 24.64q-1.625 0-3.724-.338-2.098-.27-4.061-1.354-1.896-1.083-3.182-3.249-1.218-2.234-1.218-6.092v-27.958q0-3.317 1.015-5.55 1.016-2.235 2.708-3.521 1.692-1.286 3.723-1.828 2.03-.541 3.994-.541 5.077 0 8.936.135 3.926.135 7.04.339 3.114.135 5.686.406v8.394h-18.683q-2.099 0-3.25 1.015-1.15 1.016-1.15 3.114v7.243l19.834.542v7.92l-19.835.542v6.904q0 1.76.542 2.776.61.948 1.557 1.354 1.015.338 2.098.338h18.887v8.394q-2.978.339-6.634.542-3.588.203-7.31.338-3.656.136-6.973.136zm27.392-.338v-50.093h20.715q2.978 0 5.55.744 2.573.677 4.536 2.437 1.963 1.76 3.046 4.874 1.151 3.114 1.151 7.988 0 3.453-.677 5.89t-1.828 3.993q-1.083 1.557-2.504 2.505-1.422.948-2.911 1.557l9.342 20.105h-10.222l-8.056-18.548h-1.895q-1.015-.068-2.099-.068h-2.166q-1.083 0-1.963-.067v18.683zm10.02-26.603h8.935q1.354 0 2.437-.339 1.083-.338 1.895-1.15.812-.88 1.219-2.302.473-1.422.473-3.656 0-2.098-.473-3.452-.407-1.422-1.219-2.166-.812-.813-1.895-1.084-1.083-.338-2.437-.338h-8.936zm30.235 26.603 5.822-50.093h9.612l11.508 38.382 11.44-38.382h9.545l5.89 50.093h-9.68l-4.333-36.893 1.557.135-9.816 36.758h-9.41l-9.95-36.758 1.692-.067-4.197 36.825zm71.123.339q-1.625 0-3.723-.339-2.099-.27-4.062-1.354-1.895-1.083-3.181-3.249-1.219-2.234-1.219-6.092v-27.958q0-3.317 1.016-5.55 1.015-2.235 2.707-3.521 1.693-1.286 3.723-1.828 2.031-.541 3.994-.541 5.077 0 8.936.135 3.926.135 7.04.339 3.114.135 5.686.406v8.394H576.99q-2.099 0-3.25 1.015-1.15 1.016-1.15 3.114v7.243l19.834.542v7.92l-19.834.542v6.904q0 1.76.541 2.776.61.948 1.557 1.354 1.016.338 2.099.338h18.886v8.394q-2.978.339-6.634.542-3.587.203-7.31.338-3.656.136-6.973.136zm27.393-.339v-50.093h20.714q2.979 0 5.551.744 2.572.677 4.535 2.437 1.964 1.76 3.047 4.874 1.15 3.114 1.15 7.988 0 3.453-.676 5.89-.677 2.437-1.828 3.993-1.083 1.557-2.505 2.505-1.421.948-2.91 1.557l9.341 20.105h-10.222l-8.055-18.548h-1.896q-1.015-.068-2.098-.068h-2.166q-1.084 0-1.964-.067v18.683zm10.018-26.603h8.936q1.354 0 2.437-.339 1.083-.338 1.895-1.15.813-.88 1.219-2.302.474-1.422.474-3.656 0-2.098-.474-3.452-.406-1.422-1.219-2.166-.812-.813-1.895-1.084-1.083-.338-2.437-.338h-8.936zm48.446 27.01q-4.4 0-7.785-1.016-3.317-1.015-5.686-3.723-2.302-2.708-3.52-7.717-1.15-5.077-1.15-13.133 0-7.785 1.218-12.726 1.286-5.01 3.655-7.717 2.37-2.776 5.754-3.859 3.385-1.083 7.65-1.083 3.384 0 6.295.406 2.979.338 5.348.88 2.37.474 3.994 1.083v7.785q-1.219-.27-3.317-.542-2.031-.27-4.671-.406-2.64-.203-5.551-.203-2.843 0-4.874.677-1.963.61-3.182 2.37-1.15 1.692-1.76 4.941-.541 3.25-.541 8.462 0 5.01.474 8.258.541 3.25 1.692 5.077 1.15 1.76 3.114 2.505 2.03.677 5.077.677 5.145 0 8.326-.203 3.25-.203 5.213-.474v7.717q-1.828.61-4.197 1.083-2.37.407-5.213.61-2.843.27-6.363.27zm18.796-.407 15.705-50.093h12.658l15.705 50.093h-10.424l-3.182-10.492h-17.059l-3.114 10.492zm15.772-19.496h12.32l-6.16-22zm32.944 19.496v-50.093h21.188q5.077 0 8.462 1.827 3.385 1.76 5.348 5.145 2.03 3.317 2.843 7.92.812 4.604.812 10.154 0 8.462-1.963 14.013-1.895 5.551-5.754 8.326-3.858 2.708-9.748 2.708zm10.019-9.003h10.154q3.114 0 4.941-1.76 1.828-1.828 2.64-5.416.88-3.587.88-8.868 0-4.873-.541-7.987-.542-3.182-1.625-4.942-1.015-1.76-2.64-2.437-1.557-.677-3.655-.677h-10.154zm54.538 9.41q-5.145 0-9.003-.948-3.859-1.016-6.5-3.656-2.571-2.708-3.858-7.717-1.286-5.01-1.286-13.065t1.286-13.065q1.354-5.077 3.927-7.785 2.572-2.707 6.43-3.723 3.86-1.015 9.004-1.015 5.145 0 9.003 1.015 3.859 1.016 6.431 3.723 2.572 2.708 3.859 7.785 1.286 5.01 1.286 13.065 0 8.056-1.286 13.065-1.287 5.01-3.859 7.717-2.572 2.64-6.43 3.656-3.86.947-9.004.947zm0-9.004q3.046 0 5.077-.677 2.03-.677 3.181-2.37 1.219-1.76 1.76-4.94.542-3.25.542-8.395 0-5.415-.541-8.665-.542-3.249-1.76-4.941-1.151-1.76-3.182-2.37-2.031-.609-5.077-.609-2.911 0-4.942.61-2.03.609-3.317 2.369-1.218 1.692-1.828 4.941-.541 3.25-.541 8.665 0 5.145.474 8.394.541 3.182 1.76 4.942 1.218 1.692 3.25 2.37 2.098.676 5.144.676z" style="font-weight:700;font-size:67.6939px;line-height:1;font-family:Exo;-inkscape-font-specification:'Exo Bold';text-align:center;letter-spacing:-.835595px;word-spacing:.352572px;text-anchor:middle;display:inline;fill:#f97e59;fill-opacity:1;stroke-width:2.82059;stroke-linecap:round;stroke-linejoin:round;paint-order:stroke fill markers" aria-label="SUPERMERCADO" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
        <g style="display:inline" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)">
            <path style="display:inline;fill:#fd8a77;fill-opacity:1;stroke-width:35;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M899.703 504.25h82.047V773h-82.047zM128.25 504.25h74.268V773H128.25z"/>
            <path style="display:inline;fill:#e77864;fill-opacity:1;stroke:#e77864;stroke-width:.2;stroke-linecap:butt;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers stroke fill" d="M160.088 504.35v18.035h-31.736v.576h11.935v17.283h-11.935v.576h31.736v17.284h-31.736v.576h11.935v17.285h-11.935v.574h31.736v17.285h-31.736v.576h11.935v17.284h-11.935v.576h31.736v17.285h-31.736v.574h11.935v17.285h-11.935v.576h31.736v17.284h-31.736v.576h11.935v17.285h-11.935v.574h31.736v17.285h-31.736v.577h11.935v17.283h-11.935v.576h31.736v17.283h-31.736v.576h11.935v17.285h-11.935v.577h31.736v17.283h-31.736V773h64.046v-.576h-31.736V755.14h31.736v-.577h-11.937V737.28h11.937v-.576h-31.736V719.42h31.736v-.576h-11.937V701.56h11.937v-.577h-31.736V683.7h31.736v-.574h-11.937V665.84h11.937v-.576h-31.736V647.98h31.736v-.576h-11.937V630.12h11.937v-.574h-31.736V612.26h31.736v-.576h-11.937V594.4h11.937v-.576h-31.736V576.54h31.736v-.574h-11.937V558.68h11.937v-.576h-31.736V540.82h31.736v-.576h-11.937v-17.283h11.937v-.576h-31.736V504.35zm789.148 0v18.035H917.5v.576h11.936v17.283H917.5v.576h31.736v17.284H917.5v.576h11.936v17.285H917.5v.574h31.736v17.285H917.5v.576h11.936v17.284H917.5v.576h31.736v17.285H917.5v.574h11.936v17.285H917.5v.576h31.736v17.284H917.5v.576h11.936v17.285H917.5v.574h31.736v17.285H917.5v.577h11.936v17.283H917.5v.576h31.736v17.283H917.5v.576h11.936v17.285H917.5v.577h31.736v17.283H917.5V773h64.047v-.576H949.81V755.14h31.736v-.577h-11.938V737.28h11.938v-.576H949.81V719.42h31.736v-.576h-11.938V701.56h11.938v-.577H949.81V683.7h31.736v-.574h-11.938V665.84h11.938v-.576H949.81V647.98h31.736v-.576h-11.938V630.12h11.938v-.574H949.81V612.26h31.736v-.576h-11.938V594.4h11.938v-.576H949.81V576.54h31.736v-.574h-11.938V558.68h11.938v-.576H949.81V540.82h31.736v-.576h-11.938v-17.283h11.938v-.576H949.81V504.35zm-808.37 18.61h39.019v17.284h-39.02zm789.148 0h39.02v17.284h-39.02zm-789.149 35.72h39.02v17.285h-39.02zm789.149 0h39.02v17.285h-39.02zM140.865 594.4h39.02v17.284h-39.02zm789.149 0h39.02v17.284h-39.02zm-789.149 35.72h39.02v17.284h-39.02zm789.149 0h39.02v17.284h-39.02zm-789.149 35.72h19.223v.002h.574v-.002h19.223v17.285h-39.02zm789.149 0h19.222v.002h.575v-.002h19.222v17.285h-39.02zm-789.149 35.72h39.02v17.284h-39.02zm789.149 0h39.02v17.284h-39.02Zm-789.149 35.72h39.02v17.284h-39.02zm789.149 0h39.02v17.284h-39.02z"/>
            <path style="display:inline;fill:#f9daa3;fill-opacity:1;stroke-width:35;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M192.5 504.25V773h367.633V525h176.453v248H917.5V504.25Z"/>
            <rect style="display:inline;fill:url(#b);stroke-width:35;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" width="889.358" height="26.176" x="110.321" y="478.348" ry="2.917"/>
        </g>
        <g style="display:inline">
            <path style="display:inline;fill:#d3e5fd;fill-opacity:1;stroke:none;stroke-width:6;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M207.328 524.5h327.867v202.165H207.328z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
            <path style="display:inline;fill:none;fill-opacity:1;stroke:#9b633d;stroke-width:6;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M207.328 524.5h327.867v202.165H207.328z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
            <path style="display:inline;fill:#bd825a;stroke-linecap:round;paint-order:stroke fill markers" d="M201.828 519v213.166h338.867V519Zm6 6h80.15v23.063h-80.15zm82.27 0h80.119v23.063h-80.12zm82.238 0h80.121v23.063h-80.121zm82.24 0h80.12v23.063h-80.12zm-246.748 27.115h80.15v174.051h-80.15zm82.27 0h80.119v174.051h-80.12zm82.238 0h80.121v174.051h-80.121zm82.24 0h80.12v174.051h-80.12z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
        </g>
        <g style="display:inline">
            <path style="display:inline;fill:#d3e5fd;fill-opacity:1;stroke:none;stroke-width:6;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M394.165 525.004h141.03v201.661h-141.03z" transform="matrix(1.1244 0 0 1.1244 289.577 -416.44)"/>
            <path style="display:inline;fill:none;fill-opacity:1;stroke:#9b633d;stroke-width:6;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M393.664 524.503h141.531v202.161H393.664z" transform="matrix(1.1244 0 0 1.1244 289.577 -416.44)"/>
            <path style="display:inline;fill:#bd825a;stroke-linecap:round;paint-order:markers fill stroke" d="M388.165 519.004v213.16h152.531v-213.16Zm6 6h69.205v23.058h-69.205zm71.324 0h69.207v23.058H465.49zm-71.324 27.111h69.205v174.05h-69.205zm71.324 0h69.207v174.05H465.49z" transform="matrix(1.1244 0 0 1.1244 289.577 -416.44)"/>
        </g>
        <g style="display:inline">
            <path style="display:inline;fill:#d3e5fd;fill-opacity:1;stroke:none;stroke-width:5;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M560.133 525h176.453v23.063H560.133z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
            <path style="display:inline;fill:#9b633d;fill-opacity:1;stroke-linecap:round;paint-order:markers fill stroke" d="M354.775 521.5V773h6V554.615h171.453V773h6V521.5Zm6 6h171.453v18.063H360.775Z" transform="matrix(1.1244 0 0 1.1244 102.924 -416.44)"/>
            <path style="display:inline;fill:#bd825a;stroke-linecap:round;paint-order:markers fill stroke" d="M352.275 519v254h6V552.115h176.453V773h6V519Zm6 6h176.453v23.063H358.275Z" transform="matrix(1.1244 0 0 1.1244 102.924 -416.44)"/>
        </g>
        <g style="display:inline" transform="translate(0 -250)">
            <circle style="fill:#848484;fill-opacity:1;stroke:none;stroke-width:.05;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" cx="943.546" cy="431.247" r="18.827"/>
            <circle style="fill:#8e0000;fill-opacity:1;stroke:none;stroke-width:.0415493;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" cx="943.546" cy="431.247" r="15.645"/>
            <path style="fill:#ffc3c3;fill-opacity:1;stroke:none;stroke-width:.036385;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M931.51 437.719a13.7 13.7 0 0 0 12.035 7.228 13.7 13.7 0 0 0 12.035-7.224 14.825 14.825 0 0 1-12.035 6.224 14.825 14.825 0 0 1-12.035-6.228z"/>
        </g>
    </g>
</svg>
"""
svg_Page5_PE = """
<svg width="1000" height="500" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="a">
            <stop style="stop-color:#723636;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#572b2b;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="b" x1="192.703" y1="487.034" x2="192.877" y2="499.26" gradientUnits="userSpaceOnUse"/>
    </defs>
    <g style="display:inline">
        <path style="display:inline;fill:#d3e5fd;fill-opacity:1;stroke:none;stroke-width:5;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M562.633 554.615h85.727V773h-85.727z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
        <path style="display:inline;fill:#9b633d;fill-opacity:1;stroke:#9b633d;stroke-width:.05;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M646.86 554.021h1.5V773h-1.5z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
    </g>
</svg>
"""
svg_Page5_PD = """
<svg width="1000" height="500" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="a">
            <stop style="stop-color:#723636;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#572b2b;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="b" x1="192.703" y1="487.034" x2="192.877" y2="499.26" gradientUnits="userSpaceOnUse"/>
    </defs>
    <g style="display:inline">
        <path style="display:inline;fill:#d3e5fd;fill-opacity:1;stroke:none;stroke-width:5;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M648.36 554.615h85.727V773H648.36z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
        <path style="display:inline;fill:#9b633d;fill-opacity:1;stroke:#9b633d;stroke-width:.05;stroke-linecap:round;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:markers fill stroke" d="M648.36 554.396h1.5v218.979h-1.5z" transform="matrix(1.1244 0 0 1.1244 -124.046 -416.44)"/>
    </g>
</svg>
"""



class Componente(QtWidgets.QWidget):
    def __init__(self, text:str = "", expressão: str = "False", parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
            Componente QLabel {color: #fff; font-size: 25px; font-weight: bold;}
            QWidget#rectangle {background-color: #000; border-radius: 7px;}
            #ent1, #ent2, #ent3, #saida {background-color: #000; border-radius: 4px;}
            #saidaLed{border-radius: 15px;}
        """)
        self.setFixedSize(225, 128)

        self.expressão = expressão

        self.ents = [False, False, False]

        self.ent1 = QtWidgets.QFrame(parent=self)
        self.ent1.setObjectName("ent1")
        self.ent1.setFixedSize(30, 8)
        self.ent1.move(50, 10)
        self.btEnt1 = QtWidgets.QPushButton(parent=self, text="A: Off")
        self.btEnt1.setCursor(QtCore.Qt.PointingHandCursor)
        self.btEnt1.clicked.connect(lambda: self.setEnt(0))
        self.btEnt1.move(0, 0)

        self.ent2 = QtWidgets.QFrame(parent=self)
        self.ent2.setObjectName("ent2")
        self.ent2.setFixedSize(30, 8)
        self.ent2.move(50, 60)
        self.btEnt2 = QtWidgets.QPushButton(parent=self, text="B: Off")
        self.btEnt2.setCursor(QtCore.Qt.PointingHandCursor)
        self.btEnt2.clicked.connect(lambda: self.setEnt(1))
        self.btEnt2.move(0, 51)

        self.ent3 = QtWidgets.QFrame(parent=self)
        self.ent3.setObjectName("ent3")
        self.ent3.setFixedSize(30, 8)
        self.ent3.move(50, 110)
        self.btEnt3 = QtWidgets.QPushButton(parent=self, text="C: Off")
        self.btEnt3.setCursor(QtCore.Qt.PointingHandCursor)
        self.btEnt3.clicked.connect(lambda: self.setEnt(2))
        self.btEnt3.move(0, 101)

        self.btEnts = [self.btEnt1, self.btEnt2, self.btEnt3]

        self.saida = QtWidgets.QFrame(parent=self)
        self.saida.setObjectName("saida")
        self.saida.setFixedSize(30, 8)
        self.saida.move(170, 60)

        self.saidaLed = QtWidgets.QFrame(parent=self)
        self.saidaLed.setObjectName("saidaLed")
        self.saidaLed.setFixedSize(30, 30)
        self.saidaLed.setStyleSheet("background-color: #b0b0b0;")
        self.saidaLed.move(195, 48)

        self.rectangle = QtWidgets.QFrame(parent=self)
        self.rectangle.setObjectName("rectangle")
        self.rectangle.setFixedSize(100, 128)
        self.rectangle.move(75, 0)

        self.text = QtWidgets.QLabel(parent=self, text=text)
        self.text.setFixedSize(100, 128)
        self.text.move(75, 0)
        self.text.setAlignment(Qt.AlignCenter)

        self.updateOut()
        
    @QtCore.Slot(int)
    def setEnt(self, ent:int):
        self.ents[ent] = not self.ents[ent]
        self.btEnts[ent].setText(f"{chr(65+ent)}: {'On' if self.ents[ent] else 'Off'}")
        # self.btEnts[ent].setStyleSheet("background-color: green;" if self.ents[ent] else "background-color: red;")
        
        self.updateOut()
    
    def updateOut(self):
        A = self.ents[0]
        B = self.ents[1]
        C = self.ents[2]

        saída = eval(self.expressão)
        self.saidaLed.setStyleSheet("background-color: green;" if saída else "background-color: #b0b0b0;")


class Page1(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = [], position: list = []):
        super().__init__(parent)
        self.useHardware = False

        self.Ents = [False, False, False]

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(60)

        for i, comp in enumerate(components, start=1):
            component = Componente(expressão=comp, text=str(i), parent=self)

            self.Layout.addWidget(component, *position[i-1])

    @QtCore.Slot(list)
    def updateSimulation(self, data: list):
        # print(f"Data Page 1: {data}")
        return

class Page2(QtWidgets.QWidget):
    setUseHardware = QtCore.Signal(bool)
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = []):
        super().__init__(parent)

        self.useHardware = False
        self.components = components

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(20)

        self.image = QSvgWidget(parent=self)
        self.image.renderer().load(svg_Page3.encode("utf-8"))
        self.image.setFixedSize(400, 400)

        self.imageON = QSvgWidget(parent=self.image)
        self.imageON.renderer().load(svg_Page3_ON.encode("utf-8"))
        self.imageON.setFixedSize(400, 400)

        self.imageON.hide()

        self.btnA = QtWidgets.QPushButton(parent=self.image, text="A: Off")
        self.btnA.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnA.move(100, 45)

        self.btnB = QtWidgets.QPushButton(parent=self.image, text="B: Off")
        self.btnB.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnB.move(100, 82)

        self.btnC = QtWidgets.QPushButton(parent=self.image, text="C: Off")
        self.btnC.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnC.move(285, 150)

        self.btnA.clicked.connect(lambda: self.setEnt(0))
        self.btnB.clicked.connect(lambda: self.setEnt(1))
        self.btnC.clicked.connect(lambda: self.setEnt(2))

        self.btnEnts = [self.btnA, self.btnB, self.btnC]
        self.Ents = [False, False, False]

        componentsItems = ["Hardware"]

        for i in range(len(components)):
            componentsItems.append(f"Componente {i+1}")

        self.ComboBox = QtWidgets.QComboBox(parent=self, placeholderText="Selecione um componente")
        self.ComboBox.addItems(componentsItems)
        self.ComboBox.setFixedHeight(32)
        self.ComboBox.setCursor(QtCore.Qt.PointingHandCursor)

        self.ComboBox.currentIndexChanged.connect(self.selectSimulation)

        self.Layout.addWidget(self.image, 0, 0)
        self.Layout.addWidget(self.ComboBox, 1, 0)

    @QtCore.Slot(int)
    def selectSimulation(self, index: int):
        if index == 0:
            self.useHardware = True
            self.setUseHardware.emit(True)
        else:
            self.useHardware = False
            self.setUseHardware.emit(False)
        pass

    @QtCore.Slot(int)
    def setEnt(self, ent:int):
        self.Ents[ent] = not self.Ents[ent]
        self.btnEnts[ent].setText(f"{chr(65+ent)}: {'On' if self.Ents[ent] else 'Off'}")
    
    @QtCore.Slot(list)
    def updateSimulation(self, data: list):
        if self.ComboBox.currentIndex() > 0:
            A = self.Ents[0]
            B = self.Ents[1]
            C = self.Ents[2]

            O = eval(self.components[self.ComboBox.currentIndex()-1])
            self.imageON.show() if O else self.imageON.hide()

class Page3(QtWidgets.QWidget):
    setUseHardware = QtCore.Signal(bool)
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = []):
        super().__init__(parent)

        self.useHardware = False
        self.components = components

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(20)

        self.image = QSvgWidget(parent=self)
        self.image.renderer().load(svg_Page2.encode("utf-8"))
        self.image.setFixedSize(400, 400)

        self.imageON = QSvgWidget(parent=self.image)
        self.imageON.renderer().load(svg_Page2_ON.encode("utf-8"))
        self.imageON.setFixedSize(400, 400)

        self.imageON.hide()

        self.btnA = QtWidgets.QPushButton(parent=self.image, text="A: Off")
        self.btnA.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnA.move(16, 183)

        self.btnB = QtWidgets.QPushButton(parent=self.image, text="B: Off")
        self.btnB.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnB.move(250, 200)

        self.btnC = QtWidgets.QPushButton(parent=self.image, text="C: Off")
        self.btnC.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnC.move(350, 200)

        self.btnA.clicked.connect(lambda: self.setEnt(0))
        self.btnB.clicked.connect(lambda: self.setEnt(1))
        self.btnC.clicked.connect(lambda: self.setEnt(2))

        self.btnEnts = [self.btnA, self.btnB, self.btnC]
        self.Ents = [False, False, False]

        componentsItems = ["Hardware"]

        for i in range(len(components)):
            componentsItems.append(f"Componente {i+1}")

        self.ComboBox = QtWidgets.QComboBox(parent=self, placeholderText="Selecione um componente")
        self.ComboBox.addItems(componentsItems)
        self.ComboBox.setFixedHeight(32)
        self.ComboBox.setCursor(QtCore.Qt.PointingHandCursor)

        self.ComboBox.currentIndexChanged.connect(self.selectSimulation)

        self.Layout.addWidget(self.image, 0, 0)
        self.Layout.addWidget(self.ComboBox, 1, 0)

    @QtCore.Slot(int)
    def selectSimulation(self, index: int):
        if index == 0:
            self.useHardware = True
            self.setUseHardware.emit(True)
        else:
            self.useHardware = False
            self.setUseHardware.emit(False)

    @QtCore.Slot(int)
    def setEnt(self, ent:int):
        self.Ents[ent] = not self.Ents[ent]
        self.btnEnts[ent].setText(f"{chr(65+ent)}: {'On' if self.Ents[ent] else 'Off'}")
        
    @QtCore.Slot(list)
    def updateSimulation(self, data: list):
        if self.ComboBox.currentIndex() > 0:
            A = self.Ents[0]
            B = self.Ents[1]
            C = self.Ents[2]

            O = eval(self.components[self.ComboBox.currentIndex()-1])
            self.imageON.show() if O else self.imageON.hide()

class Page4(QtWidgets.QWidget):
    setUseHardware = QtCore.Signal(bool)
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = []):
        super().__init__(parent)

        self.useHardware = False
        self.components = components

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(20)

        self.image = QSvgWidget(parent=self)
        self.image.renderer().load(svg_Page4.encode("utf-8"))
        self.image.setFixedSize(400, 400)

        self.btnA = QtWidgets.QPushButton(parent=self.image, text="A: Off")
        self.btnA.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnA.move(102, 50)

        self.btnB = QtWidgets.QPushButton(parent=self.image, text="B: Off")
        self.btnB.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnB.move(167, 50)

        self.btnC = QtWidgets.QPushButton(parent=self.image, text="C: Off")
        self.btnC.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnC.move(230, 50)

        self.btnA.clicked.connect(lambda: self.setEnt(0))
        self.btnB.clicked.connect(lambda: self.setEnt(1))
        self.btnC.clicked.connect(lambda: self.setEnt(2))

        self.btnEnts = [self.btnA, self.btnB, self.btnC]
        self.Ents = [False, False, False]

        componentsItems = ["Hardware"]

        for i in range(len(components)):
            componentsItems.append(f"Componente {i+1}")

        self.ComboBox = QtWidgets.QComboBox(parent=self, placeholderText="Selecione um componente")
        self.ComboBox.addItems(componentsItems)
        self.ComboBox.setFixedHeight(32)
        self.ComboBox.setCursor(QtCore.Qt.PointingHandCursor)

        self.ComboBox.currentIndexChanged.connect(self.selectSimulation)

        self.Layout.addWidget(self.image, 0, 0)
        self.Layout.addWidget(self.ComboBox, 1, 0)

    @QtCore.Slot(int)
    def selectSimulation(self, index: int):
        if index == 0:
            self.useHardware = True
            self.setUseHardware.emit(True)
        else:
            self.useHardware = False
            self.setUseHardware.emit(False)

    @QtCore.Slot(int)
    def setEnt(self, ent:int):
        self.Ents[ent] = not self.Ents[ent]
        self.btnEnts[ent].setText(f"{chr(65+ent)}: {'On' if self.Ents[ent] else 'Off'}")

    @QtCore.Slot(list)
    def updateSimulation(self, data: list):
        # print(f"Data Page 4: {data}")
        return

class Page5(QtWidgets.QWidget):
    setUseHardware = QtCore.Signal(bool)
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = []):
        super().__init__(parent)

        self.useHardware = False
        self.components = components

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(20)


        self.image = QSvgWidget(parent=self)
        self.image.renderer().load(svg_Page5_S.encode("utf-8"))
        self.image.setFixedSize(550, 275)

        self.image_PE = QSvgWidget(parent=self.image)
        self.image_PE.renderer().load(svg_Page5_PE.encode("utf-8"))
        self.image_PE.setFixedSize(550, 275)

        self.image_PD = QSvgWidget(parent=self.image)
        self.image_PD.renderer().load(svg_Page5_PD.encode("utf-8"))
        self.image_PD.setFixedSize(550, 275)

        self.image_S = QSvgWidget(parent=self.image)
        self.image_S.renderer().load(svg_Page5_S.encode("utf-8"))
        self.image_S.setFixedSize(550, 275)


        self.btnA = QtWidgets.QPushButton(parent=self.image, text="A: Off")
        self.btnA.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnA.move(310, 68)

        self.btnB = QtWidgets.QPushButton(parent=self.image, text="B: Off")
        self.btnB.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnB.move(370, 150)

        self.btnC = QtWidgets.QPushButton(parent=self.image, text="C: Off")
        self.btnC.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnC.move(497, 115)

        self.btnA.clicked.connect(lambda: self.setEnt(0))
        self.btnB.clicked.connect(lambda: self.setEnt(1))
        self.btnC.clicked.connect(lambda: self.setEnt(2))

        self.btnEnts = [self.btnA, self.btnB, self.btnC]
        self.Ents = [False, False, False]

        componentsItems = ["Hardware"]

        for i in range(len(components)):
            componentsItems.append(f"Componente {i+1}")

        self.ComboBox = QtWidgets.QComboBox(parent=self, placeholderText="Selecione um componente")
        self.ComboBox.addItems(componentsItems)
        self.ComboBox.setFixedHeight(32)
        self.ComboBox.setCursor(QtCore.Qt.PointingHandCursor)

        self.ComboBox.currentIndexChanged.connect(self.selectSimulation)

        self.Layout.addWidget(self.image, 0, 0)
        self.Layout.addWidget(self.ComboBox, 1, 0)

    @QtCore.Slot(int)
    def selectSimulation(self, index: int):
        if index == 0:
            self.useHardware = True
            self.setUseHardware.emit(True)
        else:
            self.useHardware = False
            self.setUseHardware.emit(False)

    @QtCore.Slot(int)
    def setEnt(self, ent:int):
        self.Ents[ent] = not self.Ents[ent]
        self.btnEnts[ent].setText(f"{chr(65+ent)}: {'On' if self.Ents[ent] else 'Off'}")

    @QtCore.Slot(list)
    def updateSimulation(self, data: list):
        if self.ComboBox.currentIndex() > 0:
            A = self.Ents[0]
            B = self.Ents[1]
            C = self.Ents[2]

            O = eval(self.components[self.ComboBox.currentIndex()-1])

            if O:
                self.image_PE.move(-45, 0)
                self.image_PD.move(45, 0)
            else:
                self.image_PE.move(0, 0)
                self.image_PD.move(0, 0)



class Projeto(QtWidgets.QWidget):
    # updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.useHardware = False
        
        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(30)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.Layout.addWidget(self.stackedWidget)

        comp1 = "A and (B or C)"
        comp2 = "A and not (B and C)"
        comp3 = "(not A) and (not B) and (C)"
        comp4 = "A and (B != C)"

        components = [comp1, comp2, comp3, comp4]
        position = [[0,0], [0,1], [1,0], [1,1]]

        self.page1 = Page1(components=components, position=position, parent=self.stackedWidget)
        self.page2 = Page2(parent=self.stackedWidget, components=components)
        self.page3 = Page3(parent=self.stackedWidget, components=components)
        self.page4 = Page4(parent=self.stackedWidget, components=components)
        self.page5 = Page5(parent=self.stackedWidget, components=components)

        self.page2.setUseHardware.connect(self.toggleUseHardware)
        self.page3.setUseHardware.connect(self.toggleUseHardware)
        self.page4.setUseHardware.connect(self.toggleUseHardware)
        self.page5.setUseHardware.connect(self.toggleUseHardware)

        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)
        self.stackedWidget.addWidget(self.page3)
        self.stackedWidget.addWidget(self.page4)
        self.stackedWidget.addWidget(self.page5)

        self.stackedWidget.setCurrentIndex(0)
        # self.stackedWidget.setCurrentIndex(4)

        self.btTo2 = QtWidgets.QPushButton(parent=self, text="Próximo")
        self.btTo2.clicked.connect(self.nextPage)
        self.btTo2.setCursor(QtCore.Qt.PointingHandCursor)
        self.Layout.addWidget(self.btTo2)

    @Slot(bool)
    def toggleUseHardware(self, useHardware: bool):
        self.useHardware = useHardware
        pass

    @Slot()
    def nextPage(self):
        c = self.stackedWidget.currentIndex()
        count = self.stackedWidget.count() - 1

        if c < count:
            c = c+1
            self.stackedWidget.setCurrentIndex(c)
        else:
            c = 0
            self.stackedWidget.setCurrentIndex(c)

        self.useHardware = self.stackedWidget.currentWidget().useHardware

        if c == count:
            self.btTo2.setText("Voltar")
        else:
            self.btTo2.setText("Próximo")
        
    @Slot()
    def resetSimulation(self):
        pass

    @Slot(list)
    def updateSimulation(self, data: list):
        self.stackedWidget.currentWidget().updateSimulation(data)
        pass

    @Slot()
    def getValues(self):
        self.values[0] = str(int(self.stackedWidget.currentWidget().Ents[0]))
        self.values[1] = str(int(self.stackedWidget.currentWidget().Ents[1]))
        self.values[2] = str(int(self.stackedWidget.currentWidget().Ents[2]))
        
        return self.values