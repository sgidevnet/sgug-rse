Name:       loook
Version:    0.8.1
Release:    15%{?dist}
Summary:    OpenOffice.org document search tool

License:    GPLv2+
URL:        http://mechtilde.de/Loook/
Source0:    http://mechtilde.de/Loook/Downloads/%{name}-%{version}.tar.gz


BuildArch:  noarch

Requires:   python3-tkinter
Requires:   hicolor-icon-theme

BuildRequires: python3-devel
BuildRequires: desktop-file-utils


%description
Loook is a simple Python tool that searches for text strings in OpenOffice.org
(and StarOffice 6.0 or later) files. It works under Linux, Windows and
Macintosh. AND, OR and phrase searches are supported. It doesn't create an
index, but searching should be fast enough unless you have really many files.


%prep
%setup -q


%build


%install
%{__rm} -rf $RPM_BUILD_ROOT
install -Dpm 0755 %{name}.py $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py
mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -s %{python3_sitelib}/%{name}/%{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 0644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/hicolor/icons/24x24/%{name}.png
install -Dpm 0644 man/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

for LANG in de nl en; do
  install -Dpm 0644 locale/$LANG/LC_MESSAGES/%{name}-%{version}.mo \
    $RPM_BUILD_ROOT%{_datadir}/locale/$LANG/LC_MESSAGES/%{name}-%{version}.mo
done

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

%find_lang %{name}-%{version}

%files -f %{name}-%{version}.lang
%{python3_sitelib}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/hicolor/icons/24x24/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-12
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-10
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.1-8
- Rebuild for brp-python-bytecompile

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Lukas Zapletal <lzap+rpm@redhat.com> 0.8.1-1
- Bumped to 0.8.1 upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.7-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 0.6.7-9
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 0.6.7-5
- adding missing build require desktop-file-utils
* Thu Nov 11 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 0.6.7-4
- Fixing issues reported by Hans de Goede
- Desktop icon properly added
* Thu Nov 11 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 0.6.7-3
- Fixing issues reported by Thomas Spura
* Thu Nov 04 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 0.6.7-2
- Fixing issues reported by Thomas Spura
* Thu Nov 04 2010 Lukas Zapletal <lzap+rpm@redhat.com> - 0.6.7-1
- Initial package
