%global pypi_name cssmin

Name:       python-cssmin
Version:    0.2.0
Release:    20%{?dist}
Summary:    A Python port of the YUI CSS compression algorithm

License:    BSD
URL:        http://github.com/zacharyvoase/cssmin
Source0:    https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:     python-cssmin-rename-bin.patch

BuildArch:  noarch
BuildRequires:  python3-devel python3-setuptools

%global _description\
A Python port of the YUI CSS compression algorithm. The library can be used for\
merging and compressing CSS files.

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}
Requires:   python3-setuptools

%description -n python3-%{pypi_name}
%{description}

This is the version for Python 3.x.


%prep
%setup -q -n %{pypi_name}-%{version}
%patch0 -p1

# remove shebang from non-executable
sed '1{\@^#!/usr/bin/env python@d}' src/cssmin.py > src/cssmin.py.new &&
touch -r  src/cssmin.py src/cssmin.py.new &&
mv src/cssmin.py.new src/cssmin.py

sed -i 's/^from distribute_setup/#/' setup.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build -O1 --root %{buildroot}

%check
cd src && \

%{__python3} -c 'import cssmin; cssmin.cssmin("""\
#href { \
  font-size: 3; \
}""")'; \

%files -n python3-cssmin
%{python3_sitelib}/cssmin.py
%{python3_sitelib}/__pycache__/cssmin.*.py*
%{python3_sitelib}/*.egg-info
%{_bindir}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.2.0-14
- Remove Python 2 Subpackage, fix #1666183

* Sat Jul 28 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.2.0-13
- Move the binary into python3-cssmin

* Sun Jul 22 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.2.0-12
- Modernize spec file
- Use python2 macros instead of python to build python2 subpackage
- Use python3 for binary
- Drop Support for EL6, EL7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-8
- Python 2 binary package renamed to python2-cssmin
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Martin Krizek <mkrizek@redhat.com> - 0.2.0-1
- Update to 0.2.0
- Add setuptools as requires
- Rename /usr/bin/cssmin (#1048622)

* Tue Oct 15 2013 Martin Krizek <mkrizek@redhat.com> - 0.1.4-6
- Fix building on f20 and higher

* Wed Oct 09 2013 Martin Krizek <mkrizek@redhat.com> - 0.1.4-5
- Add python3-setuptools as BuildRequires

* Tue Oct 08 2013 Martin Krizek <mkrizek@redhat.com> - 0.1.4-4
- Describe the package in more detail

* Mon Oct 07 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.4-3
- Add python3 subpackage and modify %%check section

* Mon Oct 07 2013 Martin Krizek <mkrizek@redhat.com> - 0.1.4-2
- Add python3-devel as dep
- Add check section

* Tue Oct 01 2013 Martin Krizek <mkrizek@redhat.com> - 0.1.4-1
- Initial packaging
