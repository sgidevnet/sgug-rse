Name:           irclog2html
Version:        2.17.2
Release:        2%{?dist}
Summary:        A script to convert IRC logs to HTML and other formats

License:        GPLv2+
URL:            http://mg.pov.lt/irclog2html/
Source0:        https://github.com/mgedmin/irclog2html/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
irclog2html is a nice IRC log parser and colorizer that will do the most common
things necessary to make an IRC log readable in a web browser. It can export to
many different HTML formats, and can export MediaWiki pipe-table syntax.

%prep
%autosetup
echo "You may need the irclog.css file. It is available at
  %{_datadir}/%{name}/irclog.css
" > README.fedora

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dpm 0644 src/%{name}/irclog.css %{buildroot}%{_datadir}/%{name}

%files
%doc CHANGES.rst HACKING.rst README.rst README.fedora
%license COPYING
%{_bindir}/%{name}
%{_bindir}/irclogsearch
%{_bindir}/irclogserver
%{_bindir}/logs2html
%{_datadir}/%{name}/
%{python3_sitelib}/%{name}/
%{python3_sitelib}/*.egg-info

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.17.2-1
- Update to latest upstream release 2.17.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.17.1-1
- Update to latest upstream release 2.17.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.15.3-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.15.3-1
- Update to latest upstream release 2.15.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.15.2-2
- Rebuild for Python 3.6

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.15.2-1
- Update to latest upstream release 2.15.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015  Fabian Affolter <mail@fabian-affolter.ch> - 2.14.0-3
- Switch to Python 3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.14.0-1
- Update to new upstream version 2.14.0

* Mon Jun 09 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.13.1-1
- Update to new upstream version 2.13.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.13.0-1
- Update to new upstream version 2.13.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.12.1-2
- Fix source URL
- Spec file cleaned

* Wed May 08 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.12.1-1
- Update to new upstream version 2.12.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.11.0-1
- Update to new upstream version 2.11.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.10.0-4
- Missing build add (#821438)

* Mon May 14 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.10.0-3
- BR update

* Mon May 14 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.10.0-2
- Install section fixed

* Sun Apr 29 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.10.0-1
- Switch to usage of the provided tarball
- Update to new upstream version 2.10.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.2-2
- Rebuilt

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.2-1
- Update to new upstream version 2.9.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 2.8-2
- Rebuilt

* Thu Jul 22 2010 Ian Weller <iweller@redhat.com> - 2.8-1
- Update to 2.8
- Add make check
- Add README.txt and CHANGES.txt to docs

* Fri Nov  6 2009 Ian Weller <ian@ianweller.org> - 2.7-5.svn68
- Fix bug (use of undefined variable 'progname') found by Ondrej Baudys

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4.svn67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3.svn67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ian Weller <ianweller@gmail.com> 2.7-2.svn67
- Fix buildroot
- Fix how-to-create-source comment

* Thu Dec 04 2008 Ian Weller <ianweller@gmail.com> 2.7-1.svn67
- Initial package build.
