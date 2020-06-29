Name:           python-flexmock
Version:        0.10.4
Release:        7%{?dist}
Summary:        Testing library that makes it easy to create mocks, stubs and fakes

License:        BSD
URL:            https://flexmock.readthedocs.org
Source0:        %{pypi_source flexmock}

BuildArch:      noarch

%global _description\
Flexmock is a testing library for Python that makes it easy to create mocks,\
stubs and fakes. The API is inspired by a Ruby library of the same name, but\
Python flexmock is not a clone of the Ruby version. It omits a number of\
redundancies in the Ruby flexmock API, alters some defaults, and introduces\
a number of Python-only features.\

%description %_description


%package -n python3-flexmock
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# for testing with various runners (twisted contains trial)
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-twisted

%{?python_provide:%python_provide python3-flexmock}

%description -n python3-flexmock %_description


%prep
%setup -q -n flexmock-%{version}


%build
%py3_build


%install
%py3_install


%check
PYEXECS=%{__python3} ./tests/run_tests.sh

 
%files -n python3-flexmock
%license LICENSE
%doc README.rst CHANGELOG docs/
%{python3_sitelib}/flexmock*
%{python3_sitelib}/__pycache__/flexmock*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-2
- Drop python2-flexmock

* Fri Apr 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-1
- Update to 0.10.4 for pytest 4 compatibility (#1699241)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-14
- Don't own /usr/lib/python3.7/site-packages/__pycache__

* Sat Jul 21 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.2-13
- Use versioned python macro in %%files

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 0.10.2-12
- Fix FTBFS bug #1605695

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.2-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.2-7
- Python 2 binary package renamed to python2-flexmock
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Slavek Kabrda <bkabrda@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Thu Dec 17 2015 Slavek Kabrda <bkabrda@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Fri Dec 11 2015 Slavek Kabrda <bkabrda@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 0.9.7-1
- Update to 0.9.7.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.6-1
- Update to 0.9.6.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.4-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.4-1
- Update to flexmock 0.9.4.
- The patch is now part of upstream => remove it.
- Introduce Python 3 subpackage.
- Add documentation files, that are now part of source package.

* Tue Feb 21 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.2-1
- Initial package.
