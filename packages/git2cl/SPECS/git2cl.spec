Name:           git2cl
Version:        2.0
Release:        0.16.git8373c9f%{?dist}
Summary:        Converts git logs to GNU style ChangeLog format

License:        GPLv2+
URL:            http://josefsson.org/git2cl/
# Source is generated from a git tag. This
# shows an example of producing a tar ball from
# the  2.0 tag.
# git clone http://repo.or.cz/r/git2cl.git 
# cd git2cl
# git archive --prefix=git2cl-2.0/  git2cl-2.0 | gzip -c > git2cl-2.0.tar.gz
# And finally to get git hash for use in the release.
# git checkout git2cl-2.0

Source0:        git2cl-2.0.tar.gz
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       git

%description
A quick tool to convert git logs to GNU ChangeLog format.

The tool invokes git log internally unless you pipe a log to it. 

%prep
%setup -q

%build
# Nothing to build.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 git2cl $RPM_BUILD_ROOT%{_bindir}/git2cl

%files
%{_bindir}/git2cl
%doc README COPYING

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.16.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.15.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.14.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.13.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.12.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.11.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.10.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.9.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.8.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.7.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0-0.6.git8373c9f
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.4.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.2.git8373c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 29 2010 Steve Traylen <steve.traylen@cern.ch> - 2.0-0.1.git8373c9f
- Use a git hash point in the release.

* Thu Aug 26 2010 Steve Traylen <steve.traylen@cern.ch> - 2.0-1
- Initial build.

