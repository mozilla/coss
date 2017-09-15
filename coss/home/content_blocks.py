from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class InputTextContentBlock(blocks.StructBlock):
    """Reusable component which adds a title followed by some text."""

    title = blocks.CharBlock(max_length=150,
                             help_text=('General content field, appropriate for questions, '
                                        'titles etc (max 150 chars)'))
    # Text field can accept a list of features to enable for the RichTextBlock
    text = blocks.RichTextBlock(max_length=1000,
                                required=False,
                                blank=True,
                                default='',
                                help_text=('WYSIWYG Editor for general purpose content, '
                                           '(max 1000 chars)'))
    link = blocks.URLBlock(help_text='Optional field - accepts a URL (max 200 chars)',
                           required=False,
                           max_length=200)
    link_title = blocks.CharBlock(max_length=100,
                                  required=False,
                                  help_text='Optional field - Title of the link, (max 100 chars)')

    class Meta:
        template = 'home/blocks/input_text_content_block.html'

    def clean(self, value):
        """Override clean method."""
        cdata = super(InputTextContentBlock, self).clean(value)
        errors = {}

        # Either link or text must contain data
        if not cdata.get('link') and not cdata.get('text'):
            error_msg = 'You need to add either some text or a link.'
            errors['text'] = ErrorList([error_msg])

        # If there is a link and not a link title, raise an error
        if cdata.get('link') and not cdata.get('link_title'):
            error_msg = 'You need to provide a title for the link.'
            errors['link_title'] = ErrorList([error_msg])

        # If there is a link title and not a link, raise an error
        if cdata.get('link_title') and not cdata.get('link'):
            error_msg = 'You need to provide a link for the link title.'
            errors['link'] = ErrorList([error_msg])

        if errors:
            raise ValidationError('Validation error in StructBlock', params=errors)

        return cdata


class CardContentBlock(InputTextContentBlock):
    image = ImageChooserBlock(required=False)

    class Meta:
        template = 'home/blocks/card_content_block.html'


class BottomCTAContentBlock(InputTextContentBlock):
    # Override text field to limit it to 100 chars.
    text = blocks.RichTextBlock(max_length=100,
                                required=False,
                                blank=True,
                                default='',
                                help_text=('WYSIWYG Editor for general purpose content, '
                                           '(max 100 chars)'))
    cta_link = blocks.URLBlock(help_text='Optional field - accepts a URL (max 200 chars)',
                               required=False,
                               max_length=200)
    cta_title = blocks.CharBlock(max_length=100,
                                 required=False,
                                 help_text='Optional field - Title of the link, (max 100 chars)')

    class Meta:
        template = 'home/blocks/bottom_banner_content_block.html'
