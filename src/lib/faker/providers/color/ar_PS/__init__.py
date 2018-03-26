# coding=utf-8
from __future__ import unicode_literals
from collections import OrderedDict

from .. import Provider as ColorProvider


class Provider(ColorProvider):
    all_colors = OrderedDict((
        ("أزرق أليس", "#F0F8FF"),
        ("أبيض عتيق", "#FAEBD7"),
        ("مائي", "#00FFFF"),
        ("زبرجدي", "#7FFFD4"),
        ("لازوردي", "#F0FFFF"),
        ("صوفي", "#F5F5DC"),
        ("حسائي", "#FFE4C4"),
        ("أسود", "#000000"),
        ("لوزي", "#FFEBCD"),
        ("أزرق", "#0000FF"),
        ("بنفسجي مزرق", "#8A2BE2"),
        ("بني", "#A52A2A"),
        ("خشبية", "#DEB887"),
        ("أزرق كاديتي", "#5F9EA0"),
        ("كرتوزي", "#7FFF00"),
        ("شوكولاتيّ", "#D2691E"),
        ("مرجاني", "#FF7F50"),
        ("قنطريوني", "#6495ED"),
        ("حرير الذرة", "#FFF8DC"),
        ("قرمزي", "#DC143C"),
        ("سيان", "#00FFFF"),
        ("أزرق داكن", "#00008B"),
        ("سيان داكن", "#008B8B"),
        ("عصا الدهب الغامق", "#B8860B"),
        ("رمادي داكن", "#A9A9A9"),
        ("أخضر داكن", "#006400"),
        ("خاكي داكن", "#BDB76B"),
        ("ماجنتا داكن", "#8B008B"),
        ("أخضر زيتوني داكن", "#556B2F"),
        ("برتقالي داكن", "#FF8C00"),
        ("أوركيدي داكن", "#9932CC"),
        ("أحمر داكن", "#8B0000"),
        ("سلموني داكن", "#E9967A"),
        ("أخضر بحري داكن", "#8FBC8F"),
        ("أزرق أردوازي داكن", "#483D8B"),
        ("رمادي لازوردي داكن", "#2F4F4F"),
        ("تركوازي داكن", "#00CED1"),
        ("بنفسج داكن", "#9400D3"),
        ("زهري غامق", "#FF1493"),
        ("أزرق سماوي غامق", "#00BFFF"),
        ("رمادي خافت", "#696969"),
        ("أزرق فريق دودجر", "#1E90FF"),
        ("الطوب شمت", "#B22222"),
        ("أبيض وردي", "#FFFAF0"),
        ("أخضر الغابت", "#228B22"),
        ("فوشي", "#FF00FF"),
        ("رمادي باهت", "#DCDCDC"),
        ("أبيض شبحي", "#F8F8FF"),
        ("ذهبي", "#FFD700"),
        ("ذهبي", "#DAA520"),
        ("رمادي", "#808080"),
        ("أخضر", "#008000"),
        ("أصفر مخضر", "#ADFF2F"),
        ("عسلي", "#F0FFF0"),
        ("وردي فاقع", "#FF69B4"),
        ("قسطلي", "#CD5C5C"),
        ("نيلي", "#4B0082"),
        ("سكري", "#FFFFF0"),
        ("خاكي", "#F0E68C"),
        ("لاڤندر", "#E6E6FA"),
        ("أحمر اللافندر", "#FFF0F5"),
        ("أخضر عشبي", "#7CFC00"),
        ("ليمون شيفوني", "#FFFACD"),
        ("أزرق فاتح", "#ADD8E6"),
        ("مرجاني فاتح", "#F08080"),
        ("أزرق طفولي", "#E0FFFF"),
        ("أصفر ذهبي فاتح ", "#FAFAD2"),
        ("رمادي فاتح", "#D3D3D3"),
        ("أخضر فاتح", "#90EE90"),
        ("وردي فاتح", "#FFB6C1"),
        ("سلموني فاتح", "#FFA07A"),
        ("أخضر بحري فاتح", "#20B2AA"),
        ("سماوي فاتح", "#87CEFA"),
        ("أزرق أردوازي فاتح", "#778899"),
        ("أزرق معدني فاتح", "#B0C4DE"),
        ("أصفر فاتح", "#FFFFE0"),
        ("ليمي", "#00FF00"),
        ("أخضر ليموني", "#32CD32"),
        ("كتاني", "#FAF0E6"),
        ("فوشيا", "#FF00FF"),
        ("كستنائي", "#800000"),
        ("زبرجدي متوسط", "#66CDAA"),
        ("أزرق متوسط", "#0000CD"),
        ("أوركيدي متوسط", "#BA55D3"),
        ("فوشي متوسط", "#9370DB"),
        ("أخضر بحري متوسط", "#3CB371"),
        ("أزرق أردوازي متوسط", "#7B68EE"),
        ("أخضر ربيعي متوسط", "#00FA9A"),
        ("ترموازي متوسط", "#48D1CC"),
        ("أحمر بنفسجي", "#C71585"),
        ("الأزرق متوسط", "#191970"),
        ("نعناعي كريمي", "#F5FFFA"),
        ("الوردي الضبابي", "#FFE4E1"),
        ("موكاسيني", "#FFE4B5"),
        ("أبيض نافاجو", "#FFDEAD"),
        ("كحلي", "#000080"),
        ("رباطي قديم", "#FDF5E6"),
        ("زيتوني", "#808000"),
        ("زيتوني رمادي", "#6B8E23"),
        ("برتقالي", "#FFA500"),
        ("أحمر برتقالي", "#FF4500"),
        ("أوركيدي", "#DA70D6"),
        ("ذهبي باهت", "#EEE8AA"),
        ("أخضر باهت", "#98FB98"),
        ("تركوازي باهت", "#AFEEEE"),
        ("أحمر بنفسجي باهت", "#DB7093"),
        ("بابايا", "#FFEFD5"),
        ("حنطي", "#FFDAB9"),
        ("بيرو", "#CD853F"),
        ("زهري", "#FFC0CB"),
        ("برقوقي", "#DDA0DD"),
        ("أزرق مسحوقي", "#B0E0E6"),
        ("أرجواني", "#800080"),
        ("أحمر", "#FF0000"),
        ("بني وردي", "#BC8F8F"),
        ("أزرق ملكي", "#4169E1"),
        ("بني السرج", "#8B4513"),
        ("سالموني", "#FA8072"),
        ("بني رملي", "#F4A460"),
        ("أخضر بحري", "#2E8B57"),
        ("صدفي", "#FFF5EE"),
        ("سيينا", "#A0522D"),
        ("فضي", "#C0C0C0"),
        ("أزرق سماي", "#87CEEB"),
        ("أزرق أردوازي", "#6A5ACD"),
        ("رمادي معدني", "#708090"),
        ("ثلجي", "#FFFAFA"),
        ("أخضر ربيعي", "#00FF7F"),
        ("أزرق معدني", "#4682B4"),
        ("نطي", "#D2B48C"),
        ("حذفي", "#008080"),
        ("أرجواني", "#D8BFD8"),
        ("طماطمي", "#FF6347"),
        ("تركواز", "#40E0D0"),
        ("بنفسجي", "#EE82EE"),
        ("قمحي", "#F5DEB3"),
        ("أبيض", "#FFFFFF"),
        ("دخاني قمحي", "#F5F5F5"),
        ("أصفر", "#FFFF00"),
        ("أصفر مخضر", "#9ACD3"),
    ))

    safe_colors = (
        'أسود', 'كستنائي', 'أخضر', 'كحلي', 'زيتوني',
        'أرجواني', 'حذفي', 'ليمي', 'أزرق', 'فضي',
        'رمادي', 'أصفر', 'فوشي', 'مائي', 'أبيض',
    )
