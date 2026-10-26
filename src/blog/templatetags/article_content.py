import re

from django import template
from django.utils.html import format_html, format_html_join

register = template.Library()
HEADING_PATTERN = re.compile(r"^(#{2,3})\s+(.+)$")


@register.filter
def render_article_content(content):
    blocks = re.split(r"\n\s*\n", content.replace("\r\n", "\n").replace("\r", "\n").strip())
    rendered_blocks = []

    for block in blocks:
        lines = block.splitlines()
        heading = HEADING_PATTERN.fullmatch(lines[0]) if len(lines) == 1 else None
        if heading:
            level = len(heading.group(1))
            rendered_blocks.append(
                format_html("<h{}>{}</h{}>", level, heading.group(2), level)
            )
            continue

        paragraph = format_html_join(
            "<br>",
            "{}",
            ((line,) for line in lines),
        )
        rendered_blocks.append(format_html("<p>{}</p>", paragraph))

    return format_html_join("\n", "{}", ((block,) for block in rendered_blocks))
