%global fontname foundation-icons
%global fontconf 60-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        3.0
Release:        3%{?dist}
Summary:        Foundation Icons font

License:        MIT
URL:            https://zurb.com/playground/foundation-icon-fonts-3
Source0:        https://zurb.com/playground/uploads/upload/upload/288/foundation-icons.zip
Source1:        %{name}-fontconfig.conf

Patch1:         foundation-icons-fonts-3.0-fix_css.patch

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       fontpackages-filesystem


%description
A custom collection of 283 icons that are stored in a handy font.

This package contains the TrueType font file which is typically used locally.


%package web
Requires:       %{fontname}-fonts = %{version}-%{release}
Summary:        Foundation Icons font css file

%description web
A custom collection of 283 icons that are stored in a handy font.

This package contains the CSS file for use on a webserver.


%prep
%autosetup -n foundation-icons


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

mkdir -p %{buildroot}%{_datadir}/foundation-icons-web/
cp -a foundation-icons.css %{buildroot}%{_datadir}/foundation-icons-web/


%_font_pkg -f %{fontconf} *.ttf

%files web
%{_datadir}/foundation-icons-web/


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Xavier Bachelot <xavier@bachelot.org> - 3.0-2
- Package TTF font only and add patch to fix CSS accordingly.
- Update descriptions and summaries.
- Drop commented out appstream support.

* Tue Jun 04 2019 Xavier Bachelot <xavier@bachelot.org> - 3.0-1
- Initial package.
