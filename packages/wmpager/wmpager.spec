%global snapdate 20130401
%global treeish	88ece7e5

Name:		wmpager
Version:	1.2
Release:	13.%{snapdate}git%{treeish}%{?dist}
Summary:	Simple pager docklet for the Window Maker

License:	BSD

# wmpager is long since abandoned by its' original author and now
# maintained by wmaker-dev@lists.windowmaker.org subscribers.
URL:		http://repo.or.cz/w/dockapps.git

# "snapshot" link from http://repo.or.cz/w/dockapps.git/tree/HEAD:/wmpager
# Tree-ish hash reduced to 8 chars, name and version parts are correctly
# parsed by gitweb.  However, you will get different results each time you
# try to download this file, because git-archive(1) stamps each file with
# current time.  This is how git-archive(1) works...
Source:		%{url}/snapshot/%{name}-%{version}-g%{treeish}.tar.gz

BuildRequires:  gcc
BuildRequires:	autoconf automake libXext-devel libXpm-devel

%description
wmpager offers the following features:
- allows workspace switching for up to nine workspaces
- automatically configures according to the number of workspaces
- automagically adjusts to the current workspace
- configurable look and feel

%prep
%setup -q -c

%build
cd dockapps
autoreconf -fisv
%configure
make %{?_smp_mflags}

%install
cd dockapps
%{make_install}

%files
# README contains license
%doc dockapps/README
%{_bindir}/wmpager
%{_mandir}/man1/wmpager.1*
%{_datadir}/wmpager

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2.20130401git88ece7e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Alexey I. Froloff <raorn@raorn.name> - 1.2-1.20130401git88ece7e5
- Initial build
