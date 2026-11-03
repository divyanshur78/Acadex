const logo = document.querySelector(".acedex-brand");

if (logo) {
    const mark = logo.querySelector(".acedex-mark");

    if (mark) {
        mark.innerHTML = `
            <svg class="acedex-monogram" viewBox="0 0 64 64"
                 role="img" aria-label="AcedeX">
                <defs>
                    <linearGradient id="axGradient" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#ffad52"/>
                        <stop offset="100%" stop-color="#e85c00"/>
                    </linearGradient>
                </defs>

                <!-- A: outer structure -->
                <path d="M8 53 L27 11 Q30 5 34 12 L54 53
                         L43 53 L30 25 L19 53 Z"
                      fill="#302820"/>

                <!-- Shared A/X cross stroke -->
                <path d="M18 39 L43 39 L49 48 L14 48 Z"
                      fill="#302820"/>

                <!-- X: integrated into the A -->
                <path d="M29 29 L51 53 L62 53 L37 25 Z"
                      fill="url(#axGradient)"/>

                <path d="M47 27 L58 27 L38 53 L27 53 Z"
                      fill="url(#axGradient)"/>
            </svg>`;
    }
}
