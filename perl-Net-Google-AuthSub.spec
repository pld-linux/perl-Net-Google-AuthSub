#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Google-AuthSub
Summary:	Net::Google::AuthSub - interact with sites that implement Google style AuthSub
Summary(pl.UTF-8):	Net::Google::AuthSub - współdziałaj ze stronami, które implementują styl Google AuthSub
Name:		perl-Net-Google-AuthSub
Version:	0.5
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SI/SIMONW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	edd1363bd9db1e96d2cd2d4893d62537
URL:		http://search.cpan.org/dist/Net-Google-AuthSub/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows to interact with sites that implement Google style
AuthSub.

%description -l pl.UTF-8
Moduł ten pozwala na współdziałanie ze stronami, które implementują
styl Google AuthSub.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/Google/*.pm
%{perl_vendorlib}/Net/Google/AuthSub
%{_mandir}/man3/*
