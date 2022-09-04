//Developer: Imdadullah Babu

const s = window.screen;
const w = (hacker.width = s.width);
const h = (hacker.height = s.height);
const ctx = hacker.getContext("2d");
const p = Array(Math.floor(w / 10) + 1).fill(0);
const random = (items) => items[Math.floor(Math.random() * items.length)];
const hex = "0123456789ABCDEFG".split("");

setInterval(() => {
    ctx.fillStyle = "rgba(0, 0, 0, .05)";
    ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = "green";
    p.map((v, i) => {
        ctx.fillText(random(hex), i * 10, v);
        p[i] = v >= h || v > 50 + 10000 * Math.random() ? 0 : v + 10;
    });

}, 1000 / 30);