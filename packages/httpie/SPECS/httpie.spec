%if 0%{?fedora}
%global with_python3 1
%endif

Name:           httpie
Version:        0.9.4
Release:        14%{?dist}
Summary:        A Curl-like tool for humans

License:        BSD
URL:            http://httpie.org/
Source0:        http://pypi.python.org/packages/source/h/httpie/httpie-%{version}.tar.gz
BuildArch:      noarch


%if 0%{?with_python3}
BuildRequires:  python3-devel

# Needed so we can build the manpage with help2man without fataling.
BuildRequires:  python3-pygments
BuildRequires:  python3-requests

Requires:       python3-pygments
Requires:       python3-requests

%else

BuildRequires:  python2-devel

# Needed so we can build the manpage with help2man without fataling.
BuildRequires:  python-pygments
BuildRequires:  python-requests
Requires:       python-pygments
Requires:       python-requests
%endif

%if 0%{?fedora}
BuildRequires:  help2man
%endif

Obsoletes:      python2-httpie <= 0.9.4-3
Obsoletes:      python3-httpie <= 0.9.4-3

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%prep
%setup -q
sed -i '/#!\/usr\/bin\/env/d' %{name}/__main__.py

# RHEL ships version 1.4, which works fine here.
sed -i 's/Pygments>=1.5/Pygments>=1.4/' setup.py

# RHEL ships version 2.6.0 which works fine here.
sed -i 's/requests>=2.10.0/requests>=2.6.0/' setup.py

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%else
%{__python2} setup.py build
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%else
%{__python2} setup.py install --root %{buildroot}
%endif

%if 0%{?with_python3}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%else
export PYTHONPATH=%{buildroot}%{python2_sitelib}
%endif

# Generate man pages for everything
mkdir -p %{buildroot}/%{_mandir}/man1
help2man --no-discard-stderr %{buildroot}/%{_bindir}/http > %{buildroot}/%{_mandir}/man1/http.1


%files
%doc README.rst
%license LICENSE
%{_mandir}/man1/http.1*
%{_bindir}/http

%if 0%{?with_python3}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*
%else
%{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}-%{version}*
%endif


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-8
- Fix help2man usage with python3.
  https://bugzilla.redhat.com/show_bug.cgi?id=1430733

* Mon Feb 27 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-7
- Fix missing Requires.  https://bugzilla.redhat.com/show_bug.cgi?id=1417730

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 2 2017 Ricky Elrod <relrod@redhat.com> - 0.9.4-5
- Add missing Obsoletes.

* Mon Jan 2 2017 Ricky Elrod <relrod@redhat.com> - 0.9.4-4
- Nuke python-version-specific subpackages. Just use py3 if we can.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 05 2016 Ricky Elrod <relrod@redhat.com> - 0.9.4-1
- Update to latest upstream.

* Fri Jun 03 2016 Ricky Elrod <relrod@redhat.com> - 0.9.3-4
- Add proper Obsoletes for rhbz#1329226.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.9.3-2
- Modernize python macros and subpackaging.
- Move LICENSE to %%license macro.
- Make python3 the default on modern Fedora.

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.9.3-1
- new version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Ricky Elrod <relrod@redhat.com> - 0.9.2-1
- Latest upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Jan 31 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.8.0-1
- Latest upstream release.

* Fri Oct 4 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.2-2
- Add in patch to work without having python-requests 2.0.0.

* Sat Sep 28 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.2-1
- Latest upstream release.

* Thu Sep 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-7
- Only try building the manpage on Fedora, since RHEL's help2man doesn't
  have the --no-discard-stderr flag.

* Thu Sep 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-6
- Loosen the requirement on python-pygments.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 2 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-4
- python-requests 1.2.3 exists in rawhide now.

* Sun Jun 30 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-3
- Patch to use python-requests 1.1.0 for now.

* Sat Jun 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-2
- Update to latest upstream release.

* Mon Apr 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-2
- Fix changelog messup.

* Mon Apr 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-1
- Update to latest upstream release.

* Mon Apr 8 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-3
- Fix manpage generation by exporting PYTHONPATH.

* Tue Mar 26 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-2
- Include Python3 support, and fix other review blockers.

* Mon Mar 11 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-1
- Update to latest upstream release

* Thu Jul 19 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.5-1
- Initial build.
