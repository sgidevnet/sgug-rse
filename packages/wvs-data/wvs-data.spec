# Well, for now we use the timestamp of unpacked data
# for version

# Other information can be obtained on
# http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/BOUNDARY/WVS/
# http://www.ngdc.noaa.gov/mgg/fliers/93mgg01.html

%define		WVS_date	20020219

Name:		wvs-data
Version:	0.0.%{WVS_date}
Release:	20%{?dist}
Summary:	World Vector Shoreline data

License:	Public Domain
URL:		http://www.flaterco.com/xtide/files.html
Source0:	ftp://ftp.flaterco.com/xtide/wvs.tar.bz2

BuildArch:	noarch

%description
This package contains World Vector Shoreline data, which can
be used for XTide related applications.

%prep
%setup -q -c %{name}-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__install} -c -p -m644 *.dat \
	$RPM_BUILD_ROOT%{_datadir}/%{name}


%files
%defattr(-,root,root,-)
%{_datadir}/%{name}/

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20020219-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20020219-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20020219-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20020219-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20020219-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20020219-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20020219-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.0.20020219-13
- Add dist-tag (RHBZ #1237193).

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20020219-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20020219-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20020219-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20020219-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20020219-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20020219-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20020219-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.0.20020219-5
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.0.20020219-4
- F-11: Mass rebuild

* Sun Oct 29 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.0.20020219-3
- Bump to remove %%{?dist} tag.

* Sat Oct 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Add %%{?dist} tag as CVS forces this.

* Wed Oct 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.0.20020219-2
- Directory name change.

* Wed Oct 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.0.20020219-1
- Initial packaging.
- Use 0.0.%%{date} for version.
