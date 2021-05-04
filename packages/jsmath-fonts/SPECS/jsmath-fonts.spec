
Summary: A collection of Math symbol fonts 
Name:	 jsmath-fonts 
Version: 20090708 
Release: 16%{?dist}

# derived from computer modern metafont tex sources
License: Public domain 
Url: 	 http://www.math.union.edu/~dpvc/jsmath/welcome.html 
Source0: http://www.math.union.edu/~dpvc/jsmath/download/TeX-fonts-linux.tgz 
BuildArch: noarch

BuildRequires: fontpackages-devel
Requires: fontpackages-filesystem

%description
%{summary}.


%prep

%setup -q -n TeX-fonts-linux 


%build


%install
rm -rf %{buildroot}

# fonts
mkdir -p %{buildroot}%{_fontdir}
install -p -m644 *.ttf %{buildroot}%{_fontdir}/



%_font_pkg *.ttf


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20090708-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20090708-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20090708-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20090708-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20090708-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20090708-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20090708-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090708-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090708-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090708-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090708-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090708-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090708-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090708-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 23 2009 Rex Dieter <rdieter@fedoraproject.org> 20090708-2
- use simple template

* Mon Nov 09 2009 Rex Dieter <rdieter@fedoraproject.org> 20090708-1
- lower case pkg name
- Version: 20090708 (time stamp of newest included font)
- use fontpackages-devel
- drop subpkg baggage
- Group: User Interface/X

* Sun Oct 25 2009 Rex Dieter <rdieter@fedoraproject.org> 0.0-1
- first try

