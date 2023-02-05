Name:           txt2rss
Version:        0.1
Release:        21%{?dist}
Summary:        Convert from txt to rss

License:        GPLv3
# Project hosting has been dropped and is no longer maintained
# URL:            http://code.google.com/p/%{name}/
Source0:        %{name}-01.tar.bz2
Source1:        txt2rss.1
Patch0:         txt2rss-license-block.patch
Patch1:         txt2rss-conf-path.patch
BuildArch:      noarch

%description
txt2rss is a shell script that parses a simple txt file (in a simple
format) and convert it to RSS feed file. Simple to use and intuitive,
you need to set up a config file with parameter like webmaster's name,
link of the site and others, after you just call the script with
options like <input file> and a <output file>.

%prep
%setup -q -c %{name}
%patch0 -p0 -b .license-block
%patch1 -p0 -b .conf-path

%build
# Empty build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/


%files
%doc news.txt feed.css
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1-12
- Fix build with unversioned %%{_docdir_fmt} (#992826).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 13 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.1-6
- Package no longer hosted on URL and development has stopped (Have
  sent mail to upstream author waiting for response)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 02 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-3
- man page, fixed conf file path

* Thu Aug 14 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-2
- applied license block patch

* Thu Aug 14 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-1
- Initial build
