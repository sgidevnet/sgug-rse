%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%global commit0 97293ab136c19df4c0b0fc80e9580c8624ad2df5
%global gittag0 HEAD
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           lorem-ipsum-generator
Version:        0.3.20161122git
Release:        24%{?dist}
Summary:        Generates random lorem ipsum text
BuildArch:      noarch 
License:        BSD
URL:            https://github.com/Riamse/lorem-ipsum-generator
Source0:        https://github.com/Riamse/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         lorem-ipsum-generator-fix-installed-files.patch
Patch1:         lorem-ipsum-generator-fix-desktop-file.patch
Requires:       python3-gobject
BuildRequires:  python3-devel python3-setuptools desktop-file-utils

%description
Lorem Ipsum Generator provides a GTK+ graphical user interface, a command-line
interface, and a Python module that generate random "lorem ipsum" text. The
Lorem Ipsum Generator can produce a given quantity of paragraphs or sentences
of "lorem ipsum" text. "Lorem ipsum" text is also known as "lipsum" text.

%prep
%setup -n %{name}-%{commit0} -q
%patch0 -p1
%patch1 -p1

%build
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/lorem-ipsum-generator.desktop

%files
%doc README COPYING TODO
%{_bindir}/lorem-ipsum-generator
%{_datadir}/applications/lorem-ipsum-generator.desktop
%{python3_sitelib}/lipsum/
%{python3_sitelib}/lorem_ipsum_generator-trunk-py?.?.egg-info/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20161122git-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20161122git-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Petr Viktorin <releng@fedoraproject.org> - 0.3.20161122git-21
- Use Python 3 version of gobject

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20161122git-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.20161122git-20
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20161122git-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20161122git-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20161122git-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.20161122git-16
- Rebuild for Python 3.6

* Tue Nov 22 2016 Jean-Francois Saucier <jsaucier@gmail.com> - 0.3.20161122git-15
- Add missing dependency for pygtk2-libglade

* Tue Aug 16 2016 Jean-Francois Saucier <jsaucier@gmail.com> - 0.3.20160816git-14
- Migrate to the github version and python 3
- Redo the patch for the new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.3-4
- Fix for the python 2.7 rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jan 15 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.3-2
- Fix as per the recommendations in bug #555376
- Rename patches to reflect the guidelines
- Adjust desktop file
- Expand the files section to be more explicit

* Thu Jan 14 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.3-1
- Initial build for Fedora
