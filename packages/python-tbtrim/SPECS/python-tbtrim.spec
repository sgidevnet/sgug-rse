%global pypi_name tbtrim

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        3%{?dist}
Summary:        Utility to trim Python traceback information

License:        MIT
URL:            https://github.com/gousaiyang/tbtrim
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
tbtrim is a utility to trim Python traceback information. By assigning user-
refined sys.excepthook, one can easily customize the behavior after an
exception is raise and uncaught, and just before the interpreter prints out
the given traceback and exception to sys.stderr.

In a more human-readable way, tbtrim is to let you handle the last words of
a program when it exits because of an exception.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
tbtrim is a utility to trim Python traceback information. By assigning user-
refined sys.excepthook, one can easily customize the behavior after an
exception is raise and uncaught, and just before the interpreter prints out
the given traceback and exception to sys.stderr.

In a more human-readable way, tbtrim is to let you handle the last words of
a program when it exits because of an exception.

%prep
%autosetup -n %{pypi_name}-%{version}
for file in README.md; do
  sed "s|\r||g" $file > $file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}*.egg-info/
%{python3_sitelib}/__pycache__/*

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream release 0.3.1 (rhbz#1815134)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-2
- Use upstream source (rhbz#1714006)
- Add license file

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Initial package for Fedora
