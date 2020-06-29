Name:           python-dukpy
Version:        0.3
Release:        5%{?dist}
Summary:        JavaScript runtime environment

License:        MIT
URL:            https://github.com/kovidgoyal/dukpy
Source0:        https://github.com/kovidgoyal/dukpy/archive/v%{version}/%{name}-%{version}.tar.gz

# Not upstreamed. Needs work.
Patch0:         0001-Use-the-system-copy-of-duktape.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  duktape-devel

%global _description %{expand:
dukpy is a JavaScript runtime environment for Python using the duktape
embeddable JavaScript engine. With dukpy, you can run JavaScript in Python.}

%description %_description

%package -n python3-dukpy
Summary:        %{summary}
%{?python_provide:%python_provide python3-dukpy}

%description -n python3-dukpy %_description

%prep
%autosetup -n dukpy-%{version} -p1

# This removed the bundled duktape. The files that form the "Duktape
# 1.x compatible module loading framework" remain. They are some
# compat glue that is not shipped in duktape-devel.
rm src/duktape/duk_config.h src/duktape/duktape.c src/duktape/duktape.h

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %__python3 -m pytest tests.py -v

%files -n python3-dukpy
%{python3_sitearch}/dukpy-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/dukpy.*.so
%doc README.rst
%license LICENSE.txt

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-1
- Drop python2 subpackage

* Thu Jun 13 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-1
- Initial packaging
