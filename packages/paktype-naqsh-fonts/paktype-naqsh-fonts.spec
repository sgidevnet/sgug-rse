%global fontname paktype-naqsh
%global fontconf 67-paktype

Name:	%{fontname}-fonts
Version:     4.1
Release:     11%{?dist}
Summary:     Fonts for Arabic from PakType

License:     GPLv2 with exceptions
URL:	https://sourceforge.net/projects/paktype/
Source0:    http://downloads.sourceforge.net/paktype/Individual-Release/PakType-Naqsh-%{version}.tar.gz
Source1:	%{fontconf}-naqsh.conf
BuildArch:   noarch
BuildRequires:	fontpackages-devel
Requires:   fontpackages-filesystem
Obsoletes: paktype-fonts-common < %{version}i-%{release}


%description 
The paktype-naqsh-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

%prep
%setup -q -c
rm -rf Code
# get rid of the white space (' ')
mv PakType\ Naqsh.ttf PakType_Naqsh.ttf
mv PakType\ Naqsh\ License.txt PakType_Naqsh_License.txt
mv PakType\ Naqsh\ Features.pdf PakType_Naqsh_Features.pdf

%{__sed} -i 's/\r//' PakType_Naqsh_License.txt
chmod a-x PakType_Naqsh.ttf PakType_Naqsh_License.txt PakType_Naqsh_Features.pdf

%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakType_Naqsh.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-naqsh.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-naqsh.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-naqsh.conf


%_font_pkg -f %{fontconf}-naqsh.conf PakType_Naqsh.ttf

%doc PakType_Naqsh_License.txt PakType_Naqsh_Features.pdf 

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Pravin Satpute <psatpute@redhat.com> - 4.1-1
- Upstream release 4.1

* Tue Feb 05 2013 Pravin Satpute <psatpute@redhat.com> - 4.0-3
- Upstream changed tarball

* Wed Nov 21 2012 Pravin Satpute <psatpute@redhat.com> - 4.0-2
- corrected upstream source url

* Tue Nov 20 2012 Pravin Satpute <psatpute@redhat.com> - 4.0-1
- upstream 4.0 release

* Mon Sep 03 2012 Pravin Satpute <psatpute@redhat.com> - 3.1-1
- upstream 3.1 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Pravin Satpute <psatpute@redhat.com> - 3.0-4
- obsoleted paktype-fonts-common, bug 656375

* Mon May 10 2010 Pravin Satpute <psatpute@redhat.com> - 3.0-3
- improved .conf file, bug 586785

* Thu Mar 04 2010 Pravin Satpute <psatpute@redhat.com> - 3.0-2
- upstream new release with license fix
- added .conf file as well

* Fri Feb 05 2010 Pravin Satpute <psatpute@redhat.com> - 3.0-1
- Initial build
- Split from paktype fonts
