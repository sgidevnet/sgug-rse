%global fontname amiri

%global common_desc \
Amiri is a classical Arabic typeface in Naskh style for typesetting books \
and other running text. \
 \
Amiri is a revival of the beautiful typeface pioneered in early 20th \
century by Bulaq Press in Cairo, also known as Amiria Press, after which \
the font is named.

%global common_desc_ar \
الخط الأميري خط نسخي موجه لطباعة الكتب والنصوص الطويلة. \
الخط الأميري هو إحياء ومحاكاة للخط الطباعي الجميل الذي \
تميزت به مطبعة بولاق منذ أوائل القرن العشرين، والتي عرفت \
أيضًا بالمطبعة الأميرية، ومن هنا أخذ الخط اسمه.

Name: %{fontname}-fonts
Version: 0.112
Release: 1%{?dist}
License: OFL

Source0: https://github.com/alif-type/amiri/releases/download/%{version}/Amiri-%{version}.zip
Source1: %{fontname}-quran-fontconfig.conf
Source2: %{fontname}-fontconfig.conf

BuildArch: noarch
BuildRequires: fontpackages-devel
Requires: %{name}-common = %{version}-%{release}

Summary: A classical Arabic font in Naskh style
Summary(ar): الخطوط الأميرية ذات المظهر الأنيق و التّراث العريق
URL: http://www.amirifont.org

%description
%common_desc

%description -l ar
%common_desc_ar

%package common

Summary: Common files for %{name}
Summary(ar): الملفات العامّة للخطوط الأميرية
Requires: fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%description common -l ar
%common_desc_ar

تتألف هذه الحزمة من ملفات الخط الأميري العامة.

%package -n %{fontname}-quran-fonts
Summary: Quran type of Amiri fonts
Summary(ar): النّمط القُرآني من الخط الأميري
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-quran-fonts
%common_desc

This package contains Quran type of Amiri fonts.
%description -n %{fontname}-quran-fonts -l ar
%common_desc_ar

تحتوي هذه الحُزمة على النّمط القرآني من الخط الأميري.

%prep
%setup -q -n Amiri-%{version}

%build
#Nothing to build

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p Amiri-Bold.ttf %{buildroot}%{_fontdir}/%{fontname}-bold.ttf
install -m 0644 -p Amiri-BoldSlanted.ttf %{buildroot}%{_fontdir}/%{fontname}-boldslanted.ttf
install -m 0644 -p Amiri-Regular.ttf %{buildroot}%{_fontdir}/%{fontname}-regular.ttf
install -m 0644 -p Amiri-Slanted.ttf %{buildroot}%{_fontdir}/%{fontname}-slanted.ttf
install -m 0644 -p AmiriQuran.ttf %{buildroot}%{_fontdir}/%{fontname}-quran.ttf
install -m 0644 -p AmiriQuranColored.ttf %{buildroot}%{_fontdir}/%{fontname}-quran-colored.ttf

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/67-%{fontname}-quran.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/67-%{fontname}.conf

for fontconf in 67-%{fontname}-quran.conf \
                67-%{fontname}.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

%_font_pkg -n quran -f 67-%{fontname}-quran.conf amiri-quran.ttf amiri-quran-colored.ttf

%_font_pkg -f 67-%{fontname}.conf amiri-regular.ttf amiri-slanted.ttf amiri-bold.ttf amiri-boldslanted.ttf

%files common
%license OFL.txt
%doc NEWS README README-Arabic NEWS-Arabic Documentation-Arabic.pdf

%changelog
* Sun Jan 26 2020 Mosaab Alzoubi <moceap[At]hotmail[Dot]com> - 0.112-1
- Update to 0.112

* Mon Sep 9 2019 Mosaab Alzoubi <moceap[At]hotmail[Dot]com> - 0.111-1
- Update to 0.111

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 28 2017 Mosaab Alzoubi <moceap@hotmail.com> - 0.109-1
- Update to 0.109

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.108-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Mosaab Alzoubi <moceap@hotmail.com> - 0.108-1
- New version with alot of additions and fixes
- New upstream moved to Github
- Add amiri-quran-colored font
- Use %%license macro
- Clean up spec file

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.107-1
- Update to 0.107.
- Upstream use zip instead of gz.

* Wed Nov 13 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-9
- Change variable font priority to 67 in font_pkg line.
- Reform Summary.
 
* Mon Nov 11 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-8
- Re-split into main and Quran fonts.
- Improve Amiri Quran font config.
- Add license files to -common, dropped from others.
- Drop fontpackages-filesystem requires from main package.

* Mon Nov 11 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-7
- Fix Sourceforg link in Source0.
- Decrease instructions to rebuild Amiri from the source.
- Replace -docs by -common.
- Change font priority to 67.
- Improve font config.
- The fonts in one family so it united into 1 main package instead of 2.
- -common to be main package require.

* Mon Oct 28 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-6
- Replaces define by global.

* Mon Oct 28 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-5
- Drop .woff fonts.
- Update description by official one.
- Make this package ready for building if it possible later.

* Sun Oct 20 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-4
- Drop web and meta packages.
- Many Fixes.

* Sat Oct 19 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-3
- Rewritten almost from zero.

* Thu Oct 10 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-2
- Some fixes to be compatible with Fedora rules.

* Fri Oct 4 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-1
- Update version to 0.106
- Update description by adding Amiri summary in Arabic
- Font released in two licenses (GPL2,OFL1.1)
- Make universal source

* Mon Dec 19 2011  Muayyad Salah Alsadi <alsadi@ojuba.org> - 0.100-2
- no need for web version
- make it -fonts not -font (see http://fedoraproject.org/wiki/Packaging:FontsPolicy)

* Mon Dec 19 2011  Ehab El-Gedawy <ehabsas@gmail.com> - 0.100-1
- Initial Packaging

