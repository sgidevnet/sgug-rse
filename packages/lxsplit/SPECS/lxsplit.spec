Name:		lxsplit
Version:	0.2.4
Release:	20%{?dist}
Summary:	File split / merge utility

License:	GPLv2+
URL:		http://lxsplit.sourceforge.net/
Source:		http://downloads.sourceforge.net/lxsplit/%{name}-%{version}.tar.gz
BuildRequires:	gcc

%description
lxSplit is a simple tool for splitting files and joining the splitted files 
on linux and unix-like platforms. Splitting is done without compression and 
large files (> 4 GB) are supported. lxSplit is fully compatible with the 
HJSplit utility which is available for other operating systems.



%prep
%setup -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" %{?_smp_flags}

%install
%{__mkdir_p} %{buildroot}/%{_bindir}
%{__install} -D -m755 lxsplit %{buildroot}/%{_bindir}/lxsplit

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/lxsplit

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.2.4-12
- Some clean-up according to recent packaging guidelines

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Fri Oct 03 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.4-1
- new upstream release

* Thu Jul 03 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.3-1
-  Pull new upstream. Drop obsoleted patch and fix defattr

* Sat May 31 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.2-4
- Apply upstream build patch

* Tue May 27 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.2-3
- Fixed cflags, attr and added COPYING

* Sun May 25 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.2-2
- Add dist tag

* Sun May 25 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.2-1
- Upstream spec modified for Fedora

