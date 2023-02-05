%global fontname gfs-porson
%global fontconf 61-%{fontname}.conf

%global archivename GFS_Porson_OT

Name:    %{fontname}-fonts
Version: 20060908
Release: 27%{?dist}
Summary: GFS Porson Greek font

License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces19th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{name}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
In England, during the 1790’s, Cambridge University Press decided to procure a
new set of Greek types. The university’s great scholar of Classics, Richard
Porson was asked to produce a typeface based on his handsome handwriting and
Richard Austin was commissioned to cut the types. The type was completed in
1808, after the untimely death of Porson the previous year. Its success was
immediate and since then the classical editions in Great Britain and the
U.S.A. use it, almost invariably.

In 1913, Monotype released the typeface with some corrections, notably
replacing the upright capitals suggested by Porson with inclined ones. In
Greece the typeface was used under the name Pelasgika type.

GFS Porson is based on the Monotype version, though using upright capitals, as
in the original.


%prep
%setup -q -c -T
unzip -j -L -q %{SOURCE0}
chmod 0644 *.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}



%_font_pkg -f %{fontconf} *.otf

%doc *.txt *.pdf


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-11
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-10
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-9
▤ Rebuild using new « rpm-fonts »

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-8
⌖ Fedora 10 alpha general package cleanup

* Wed Apr 30 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-7
⥁ Yet another prep fix®

* Mon Mar 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-6
⚰ RIP OSX zip metadata. You won't be missed.

* Sun Feb 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-4
⌂ Update URL

* Mon Nov 26 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☠ 20060908-3
⚑ Re-size description so the paupers that can not afford a 80th column in
their terminal are not discriminated against.
(Courtesy: the 79-column-liberation-front cell that subverted the rpmlint
codebase)

* Sun Nov 25 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 20060908-2
✓ initial packaging
