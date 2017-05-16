from mezzanine.conf import register_setting

register_setting(
    name='GITHUB_LINK',
    description='If present a Github icon linking to coss repository will be shown',
    label='Contribute',
    editable=True,
    default='https://github.com/mozilla/coss/issues',
)

register_setting(
    name='DISCOURSE_LINK',
    description='If present a Discourse icon linking to coss thread will be shown',
    editable=True,
    default='https://discourse.mozilla-community.org',
)

register_setting(
    name='LEGAL_LINK',
    description='If present an icon linking to the legal Mozilla link will be shown.',
    editable=True,
    default='https://www.mozilla.org/en-US/about/legal/',
)

register_setting(
    name='LICENSE_LINK',
    description='If present an icon linking to Mozilla license will be shown.',
    editable=True,
    default='https://www.mozilla.org/en-US/foundation/licensing/website-content/',
)
