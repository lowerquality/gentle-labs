// Make some convenience methods for generating DOM Elements
const htmltags = [
  "div",
  "a",
  "h1",
  "h2",
  "h3",
  "b",
  "i",
  "p",
  "br",
  "span",
  "hr",
  "video",
  "audio",
  "img",
  "canvas",
  "li",
  "ul",
  "ol",
  "quote",
  "pre",
  "code",
  "textarea",
  "input",
  "label",
  "button",
  "form",
  "select",
  "option",
  // SVG
  "svg",
  "line",
  "rect",
  "circle",
  "g",
  "ellipse",
  "path",
  "polyline",
  "polygon",
  "text",
  // SVG tags that share a name with HTML tags
  "a_svg" // This makes an <a> with the SVG doctype
];

export let E = {};
htmltags.forEach((tagname, idx) => {
  const is_svg = idx >= htmltags.indexOf("svg");

  let fn_name = tagname;
  if (tagname.indexOf("_svg") > 0) {
    tagname = tagname.slice(0, tagname.length - 4);
  }

  E[fn_name] = ($parent, attrs, textContent) => {
    attrs = attrs || {};
    let $el = document.createElementNS(
      is_svg ? "http://www.w3.org/2000/svg" : "http://www.w3.org/1999/xhtml",
      tagname
    );
    for (let aname in attrs) {
      $el.setAttribute(aname, attrs[aname]);
    }
    if (textContent) {
      $el.textContent = textContent;
    }
    if ($parent) {
      $parent.appendChild($el);
    }
    return $el;
  };
});
