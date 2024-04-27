#!/usr/bin/env python
# Copyright (C) 2008 Søren Roug, European Environment Agency
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#


from .namespaces import (
    ANIMNS,
    CHARTNS,
    DR3DNS,
    DRAWNS,
    FORMNS,
    MANIFESTNS,
    METANS,
    NUMBERNS,
    OFFICENS,
    PRESENTATIONNS,
    SCRIPTNS,
    STYLENS,
    SVGNS,
    TABLENS,
    TEXTNS,
)

# Inline element don't cause a box
# They are analogous to the HTML elements SPAN, B, I etc.
inline_elements = (
    (TEXTNS,'a'),
    (TEXTNS,'author-initials'),
    (TEXTNS,'author-name'),
    (TEXTNS,'bibliography-mark'),
    (TEXTNS,'bookmark-ref'),
    (TEXTNS,'chapter'),
    (TEXTNS,'character-count'),
    (TEXTNS,'conditional-text'),
    (TEXTNS,'creation-date'),
    (TEXTNS,'creation-time'),
    (TEXTNS,'creator'),
    (TEXTNS,'database-display'),
    (TEXTNS,'database-name'),
    (TEXTNS,'database-next'),
    (TEXTNS,'database-row-number'),
    (TEXTNS,'database-row-select'),
    (TEXTNS,'date'),
    (TEXTNS,'dde-connection'),
    (TEXTNS,'description'),
    (TEXTNS,'editing-cycles'),
    (TEXTNS,'editing-duration'),
    (TEXTNS,'execute-macro'),
    (TEXTNS,'expression'),
    (TEXTNS,'file-name'),
    (TEXTNS,'hidden-paragraph'),
    (TEXTNS,'hidden-text'),
    (TEXTNS,'image-count'),
    (TEXTNS,'initial-creator'),
    (TEXTNS,'keywords'),
    (TEXTNS,'measure'),
    (TEXTNS,'modification-date'),
    (TEXTNS,'modification-time'),
    (TEXTNS,'note-ref'),
    (TEXTNS,'object-count'),
    (TEXTNS,'page-continuation'),
    (TEXTNS,'page-count'),
    (TEXTNS,'page-number'),
    (TEXTNS,'page-variable-get'),
    (TEXTNS,'page-variable-set'),
    (TEXTNS,'paragraph-count'),
    (TEXTNS,'placeholder'),
    (TEXTNS,'print-date'),
    (TEXTNS,'printed-by'),
    (TEXTNS,'print-time'),
    (TEXTNS,'reference-ref'),
    (TEXTNS,'ruby'),
    (TEXTNS,'ruby-base'),
    (TEXTNS,'ruby-text'),
    (TEXTNS,'script'),
    (TEXTNS,'sender-city'),
    (TEXTNS,'sender-company'),
    (TEXTNS,'sender-country'),
    (TEXTNS,'sender-email'),
    (TEXTNS,'sender-fax'),
    (TEXTNS,'sender-firstname'),
    (TEXTNS,'sender-initials'),
    (TEXTNS,'sender-lastname'),
    (TEXTNS,'sender-phone-private'),
    (TEXTNS,'sender-phone-work'),
    (TEXTNS,'sender-position'),
    (TEXTNS,'sender-postal-code'),
    (TEXTNS,'sender-state-or-province'),
    (TEXTNS,'sender-street'),
    (TEXTNS,'sender-title'),
    (TEXTNS,'sequence'),
    (TEXTNS,'sequence-ref'),
    (TEXTNS,'sheet-name'),
    (TEXTNS,'span'),
    (TEXTNS,'subject'),
    (TEXTNS,'table-count'),
    (TEXTNS,'table-formula'),
    (TEXTNS,'template-name'),
    (TEXTNS,'text-input'),
    (TEXTNS,'time'),
    (TEXTNS,'title'),
    (TEXTNS,'user-defined'),
    (TEXTNS,'user-field-get'),
    (TEXTNS,'user-field-input'),
    (TEXTNS,'variable-get'),
    (TEXTNS,'variable-input'),
    (TEXTNS,'variable-set'),
    (TEXTNS,'word-count'),
)


# It is almost impossible to determine what elements are block elements.
# There are so many that don't fit the form
block_elements = (
    (TEXTNS,'h'),
    (TEXTNS,'p'),
    (TEXTNS,'list'),
    (TEXTNS,'list-item'),
    (TEXTNS,'section'),
)

declarative_elements = (
    (OFFICENS,'font-face-decls'),
    (PRESENTATIONNS,'date-time-decl'),
    (PRESENTATIONNS,'footer-decl'),
    (PRESENTATIONNS,'header-decl'),
    (TABLENS,'table-template'),
    (TEXTNS,'alphabetical-index-entry-template'),
    (TEXTNS,'alphabetical-index-source'),
    (TEXTNS,'bibliography-entry-template'),
    (TEXTNS,'bibliography-source'),
    (TEXTNS,'dde-connection-decls'),
    (TEXTNS,'illustration-index-entry-template'),
    (TEXTNS,'illustration-index-source'),
    (TEXTNS,'index-source-styles'),
    (TEXTNS,'index-title-template'),
    (TEXTNS,'note-continuation-notice-backward'),
    (TEXTNS,'note-continuation-notice-forward'),
    (TEXTNS,'notes-configuration'),
    (TEXTNS,'object-index-entry-template'),
    (TEXTNS,'object-index-source'),
    (TEXTNS,'sequence-decls'),
    (TEXTNS,'table-index-entry-template'),
    (TEXTNS,'table-index-source'),
    (TEXTNS,'table-of-content-entry-template'),
    (TEXTNS,'table-of-content-source'),
    (TEXTNS,'user-field-decls'),
    (TEXTNS,'user-index-entry-template'),
    (TEXTNS,'user-index-source'),
    (TEXTNS,'variable-decls'),
)

empty_elements = (
    (ANIMNS,'animate'),
    (ANIMNS,'animateColor'),
    (ANIMNS,'animateMotion'),
    (ANIMNS,'animateTransform'),
    (ANIMNS,'audio'),
    (ANIMNS,'param'),
    (ANIMNS,'set'),
    (ANIMNS,'transitionFilter'),
    (CHARTNS,'categories'),
    (CHARTNS,'data-point'),
    (CHARTNS,'domain'),
    (CHARTNS,'error-indicator'),
    (CHARTNS,'floor'),
    (CHARTNS,'grid'),
    (CHARTNS,'legend'),
    (CHARTNS,'mean-value'),
    (CHARTNS,'regression-curve'),
    (CHARTNS,'stock-gain-marker'),
    (CHARTNS,'stock-loss-marker'),
    (CHARTNS,'stock-range-line'),
    (CHARTNS,'symbol-image'),
    (CHARTNS,'wall'),
    (DR3DNS,'cube'),
    (DR3DNS,'extrude'),
    (DR3DNS,'light'),
    (DR3DNS,'rotate'),
    (DR3DNS,'sphere'),
    (DRAWNS,'contour-path'),
    (DRAWNS,'contour-polygon'),
    (DRAWNS,'equation'),
    (DRAWNS,'fill-image'),
    (DRAWNS,'floating-frame'),
    (DRAWNS,'glue-point'),
    (DRAWNS,'gradient'),
    (DRAWNS,'handle'),
    (DRAWNS,'hatch'),
    (DRAWNS,'layer'),
    (DRAWNS,'marker'),
    (DRAWNS,'opacity'),
    (DRAWNS,'page-thumbnail'),
    (DRAWNS,'param'),
    (DRAWNS,'stroke-dash'),
    (FORMNS,'connection-resource'),
    (FORMNS,'list-value'),
    (FORMNS,'property'),
    (MANIFESTNS,'algorithm'),
    (MANIFESTNS,'key-derivation'),
    (METANS,'auto-reload'),
    (METANS,'document-statistic'),
    (METANS,'hyperlink-behaviour'),
    (METANS,'template'),
    (NUMBERNS,'am-pm'),
    (NUMBERNS,'boolean'),
    (NUMBERNS,'day'),
    (NUMBERNS,'day-of-week'),
    (NUMBERNS,'era'),
    (NUMBERNS,'fraction'),
    (NUMBERNS,'hours'),
    (NUMBERNS,'minutes'),
    (NUMBERNS,'month'),
    (NUMBERNS,'quarter'),
    (NUMBERNS,'scientific-number'),
    (NUMBERNS,'seconds'),
    (NUMBERNS,'text-content'),
    (NUMBERNS,'week-of-year'),
    (NUMBERNS,'year'),
    (OFFICENS,'dde-source'),
    (PRESENTATIONNS,'date-time'),
    (PRESENTATIONNS,'footer'),
    (PRESENTATIONNS,'header'),
    (PRESENTATIONNS,'placeholder'),
    (PRESENTATIONNS,'play'),
    (PRESENTATIONNS,'show'),
    (PRESENTATIONNS,'sound'),
    (SCRIPTNS,'event-listener'),
    (STYLENS,'column'),
    (STYLENS,'column-sep'),
    (STYLENS,'drop-cap'),
    (STYLENS,'footnote-sep'),
    (STYLENS,'list-level-properties'),
    (STYLENS,'map'),
    (STYLENS,'ruby-properties'),
    (STYLENS,'table-column-properties'),
    (STYLENS,'tab-stop'),
    (STYLENS,'text-properties'),
    (SVGNS,'definition-src'),
    (SVGNS,'font-face-format'),
    (SVGNS,'font-face-name'),
    (SVGNS,'stop'),
    (TABLENS,'body'),
    (TABLENS,'cell-address'),
    (TABLENS,'cell-range-source'),
    (TABLENS,'change-deletion'),
    (TABLENS,'consolidation'),
    (TABLENS,'database-source-query'),
    (TABLENS,'database-source-sql'),
    (TABLENS,'database-source-table'),
    (TABLENS,'data-pilot-display-info'),
    (TABLENS,'data-pilot-field-reference'),
    (TABLENS,'data-pilot-group-member'),
    (TABLENS,'data-pilot-layout-info'),
    (TABLENS,'data-pilot-member'),
    (TABLENS,'data-pilot-sort-info'),
    (TABLENS,'data-pilot-subtotal'),
    (TABLENS,'dependency'),
    (TABLENS,'error-macro'),
    (TABLENS,'even-columns'),
    (TABLENS,'even-rows'),
    (TABLENS,'filter-condition'),
    (TABLENS,'first-column'),
    (TABLENS,'first-row'),
    (TABLENS,'highlighted-range'),
    (TABLENS,'insertion-cut-off'),
    (TABLENS,'iteration'),
    (TABLENS,'label-range'),
    (TABLENS,'last-column'),
    (TABLENS,'last-row'),
    (TABLENS,'movement-cut-off'),
    (TABLENS,'named-expression'),
    (TABLENS,'named-range'),
    (TABLENS,'null-date'),
    (TABLENS,'odd-columns'),
    (TABLENS,'odd-rows'),
    (TABLENS,'operation'),
    (TABLENS,'scenario'),
    (TABLENS,'sort-by'),
    (TABLENS,'sort-groups'),
    (TABLENS,'source-range-address'),
    (TABLENS,'source-service'),
    (TABLENS,'subtotal-field'),
    (TABLENS,'table-column'),
    (TABLENS,'table-source'),
    (TABLENS,'target-range-address'),
    (TEXTNS,'alphabetical-index-auto-mark-file'),
    (TEXTNS,'alphabetical-index-mark'),
    (TEXTNS,'alphabetical-index-mark-end'),
    (TEXTNS,'alphabetical-index-mark-start'),
    (TEXTNS,'bookmark'),
    (TEXTNS,'bookmark-end'),
    (TEXTNS,'bookmark-start'),
    (TEXTNS,'change'),
    (TEXTNS,'change-end'),
    (TEXTNS,'change-start'),
    (TEXTNS,'dde-connection-decl'),
    (TEXTNS,'index-entry-bibliography'),
    (TEXTNS,'index-entry-chapter'),
    (TEXTNS,'index-entry-link-end'),
    (TEXTNS,'index-entry-link-start'),
    (TEXTNS,'index-entry-page-number'),
    (TEXTNS,'index-entry-tab-stop'),
    (TEXTNS,'index-entry-text'),
    (TEXTNS,'index-source-style'),
    (TEXTNS,'line-break'),
    (TEXTNS,'page'),
    (TEXTNS,'reference-mark'),
    (TEXTNS,'reference-mark-end'),
    (TEXTNS,'reference-mark-start'),
    (TEXTNS,'s'),
    (TEXTNS,'section-source'),
    (TEXTNS,'sequence-decl'),
    (TEXTNS,'soft-page-break'),
    (TEXTNS,'sort-key'),
    (TEXTNS,'tab'),
    (TEXTNS,'toc-mark'),
    (TEXTNS,'toc-mark-end'),
    (TEXTNS,'toc-mark-start'),
    (TEXTNS,'user-field-decl'),
    (TEXTNS,'user-index-mark'),
    (TEXTNS,'user-index-mark-end'),
    (TEXTNS,'user-index-mark-start'),
    (TEXTNS,'variable-decl')
)
