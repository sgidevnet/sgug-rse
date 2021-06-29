%define stamp 20081006

Name:           uread
Version:        0
Release:        0.21.%{stamp}%{?dist}
Summary:        Utilities for unformatted fortran files

License:        GPL+
URL:            http://www.engineers.auckland.ac.nz/~snor007/software.html#uread
Source0:        uread-%{stamp}.tar.gz
# unversioned upstream source, downloaded with wget -N
# renamed to uread-YYYYMMDD.tar.gz
#Source0:        http://www.engineers.auckland.ac.nz/~snor007/src/uread.tar.gz

# this is a mail exchange where the author gives the right to redistribute 
# his work under the GPL
Source1:        uread-licence.email
#Patch0:         uread-include_stdlib.diff

#BuildRequires:  
#Requires:       


BuildRequires:  gcc
%description
These utilities enable you to have a look at a Fortran unformatted file to 
see the size of the data records, and to swap its endianess from big to 
little, or vis versa.

%prep
%setup -q -n uread
#%patch0 -p1

cp -p %{SOURCE1} .

%build
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -d -m755 $RPM_BUILD_ROOT%{_bindir}/
install -p -m644 *.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m0755 uread ustrip uswap $RPM_BUILD_ROOT%{_bindir}/



%files
%doc uread-licence.email
%{_bindir}/uread
%{_bindir}/ustrip
%{_bindir}/uswap
%{_mandir}/man1/u*.1*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20081006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 27 2009 Jon Ciesla - 0-0.4.20081006
- Updated to new release.
- Dropped patch.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.19981218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0-0.3.19981218
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Patrice Dumas <pertusus@free.fr> 0-0.2.19981218
- correct license
- keep timestamps

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0-0.1.19981218
- Rebuild for selinux ppc32 issue.
- Use proper pre-release syntax in Release.

* Tue Jun 26 2007 Patrice Dumas <pertusus@free.fr> 0-0.19981218
- use 0 as version and put the timestamp in the release

* Wed Jun 14 2006 Patrice Dumas <pertusus@free.fr> 0.19981218-1
- Initial packaging
