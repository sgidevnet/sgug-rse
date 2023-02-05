Name:    zsh-autosuggestions
Version: 0.6.4
Release: 1%{?dist}

Summary: Fish-like autosuggestions for zsh
License: MIT
URL:     https://github.com/zsh-users/zsh-autosuggestions
Source0: https://github.com/zsh-users/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: zsh

Requires: zsh

%description
This package provides autosuggestions for the shell zsh. It suggests commands
as you type based on history and completions.

%prep
%autosetup

%build
make

%install
install -D --preserve-timestamps --target-directory=%{buildroot}%{_datadir}/%{name} %{name}.zsh

%check

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_datadir}/%{name}

%changelog
* Sun Mar 01 2020 Michael Kuhn <suraia@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Sun Nov 17 2019 Michael Kuhn <suraia@fedoraproject.org> - 0.6.3-1
- Initial package
